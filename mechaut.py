DistEManc =1095
DT =420
carga =16510
file_path ="C:\\Users\\gabriel.prado\\Desktop\\AUT_TAMB_WB\\TESTE\\71396136\\out.csv"

geometry = Model.Geometry
mesh = Model.Mesh
connections = Model.Connections

ass = DataModel.GeoData.Assemblies[0]
carc = ass.Parts[0]
disc1 = ass.Parts[1]
disc2 = ass.Parts[2]
eixo = ass.Parts[3]

SM = ExtAPI.SelectionManager
subsel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)

namesel = 'EIXO'
sel_list = DataModel.GetObjectsByName(namesel)
eixo_id_list = []
for i in range(0,sel_list[0].Children.Count):
    print(sel_list.Item[0].Name)
    gb = sel_list.Item[0].Children[i].GetGeoBody()
    eixo_id_list.append(gb.Id)
print(eixo_id_list)

mesh_id = []
namesel = 'DISCO\Solid1'
sel_list = DataModel.GetObjectsByName(namesel)
disco_id_list = []
for i in range(0,sel_list.Count):
    print(sel_list.Item[i].Name)
    gb = sel_list.Item[i].GetGeoBody()
    disco_id_list.append(gb.Id)
    for face in gb.Faces:
        mesh_id.append(face.Id)

namesel = 'DISCO\Solid11'
sel_list = DataModel.GetObjectsByName(namesel)
for i in range(0,sel_list.Count):
    print(sel_list.Item[i].Name)
    gb = sel_list.Item[i].GetGeoBody()
    disco_id_list.append(gb.Id)
    for face in gb.Faces:
        mesh_id.append(face.Id)
print(disco_id_list)

namesel = 'CARC'
sel_list = DataModel.GetObjectsByName(namesel)
carc_id_list = []
for i in range(0,sel_list[0].Children.Count):
    print(sel_list.Item[0].Name)
    gb = sel_list.Item[0].Children[i].GetGeoBody()
    carc_id_list.append(gb.Id)
    for face in gb.Faces:
        mesh_id.append(face.Id)
print(carc_id_list)

#Cria Malha no Eixo
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = eixo_id_list
mesh_method = mesh.AddAutomaticMethod()
mesh_method.Location = mysel
mesh_method.Method = MethodType.Sweep

mesh_method = mesh.AddSizing()
mesh_method.Location = mysel
mesh_method.ElementSize = Quantity('11.0 [mm]')

#Cria Malha no Disco
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = disco_id_list
mesh_method = mesh.AddAutomaticMethod()
mesh_method.Location = mysel
mesh_method.Method = MethodType.HexDominant
mesh_method.FreeFaceMeshType = 2

mesh_method = mesh.AddSizing()
mesh_method.Location = mysel
mesh_method.ElementSize = Quantity('8.0 [mm]')


#Cria Malha na Carcaca
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = carc_id_list
mesh_method = mesh.AddAutomaticMethod()
mesh_method.Location = mysel
mesh_method.Method = MethodType.HexDominant
mesh_method.FreeFaceMeshType = 2

mesh_method = mesh.AddSizing()
mesh_method.Location = mysel
mesh_method.ElementSize = Quantity('16.0 [mm]')


#Cria Face Meshing
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = mesh_id
mesh_method = mesh.AddFaceMeshing()
mesh_method.Location = mysel

#Clear and Generate Mesh
mesh.ClearGeneratedData()
mesh.GenerateMesh()

#CARC
volcarc={}
aux = 0
for body in carc.Bodies:
    volcarc[aux] = body.Volume
    aux +=1
sortedvolcarc = sorted(volcarc.items(),key = lambda item:item[1])
carc_contact_id = []

carc_contact_id = []
for i in range(0,4):
    cent = {}
    aux = 0
    for face in carc.Bodies[sortedvolcarc[i][0]].Faces:
        print(face.Id,face.Centroid)
        cent [aux] = abs(face.Centroid[2])
        aux+=1
    sortedcent = sorted(cent.items(),key = lambda item:item[1])
    carc_contact_id.append(carc.Bodies[sortedvolcarc[i][0]].Faces[sortedcent[2][0]].Id)
    cent = None
carc_contact_id

#DiscSort
ldisc = {}
for face in disc1.Bodies[0].Faces:
    if face.Edges.Count==2:
        if face.Edges[0].Length == face.Edges[1].Length:
            ldisc[face.Id]=face.Edges[0].Length
sorteddisc = sorted(ldisc.items(),key = lambda item:item[1])

ldisc2 = {}
for face in disc2.Bodies[0].Faces:
    if face.Edges.Count==2:
        if face.Edges[0].Length == face.Edges[1].Length:
            ldisc2[face.Id]=face.Edges[0].Length
sorteddisc2 = sorted(ldisc2.items(),key = lambda item:item[1])

areadisc = {}
for face in disc1.Bodies[0].Faces:
    areadisc[face.Id] = face.Area
sortedareadisc = sorted(areadisc.items(),key = lambda item:item[1])
    



#DiscoCarc1
contact = Model.Connections.AddContactRegion()
contact.Activate()
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = [sorteddisc2[-1][0]]
contact.TargetLocation = mysel
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = carc_contact_id[0:2]
contact.SourceLocation = mysel

#DiscoCarc2
contact = Model.Connections.AddContactRegion()
contact.Activate()
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = [sorteddisc[-1][0]]
contact.TargetLocation = mysel
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = carc_contact_id[2:4]
contact.SourceLocation = mysel

vol = {}
aux = 0
for body in eixo.Bodies:
    vol[aux]=body.Volume
    aux+=1
sortedvol = sorted(vol.items(),key = lambda item:item[1])
start_i = 0
for i in range(len(sortedvol)):
    count = 0
    for j in range(i+1,len(sortedvol)):
        if abs(sortedvol[i][-1]-sortedvol[j][-1])<=1e-8:
            count+=1
            print(count)
            if count == 3:
                start_i =i
                break
        else:
            break
    

eix_list1 =[]
eix_list2 = []
for i in range(start_i,start_i+4):
    for face in eixo.Bodies[sortedvol[i][0]].Faces:
        if abs(abs(eixo.Bodies[sortedvol[i][0]].Centroid[0])-abs(face.Centroid[0]))<=0.0001:
            if face.Centroid[0]<0:
                eix_list1.append(face.Id)
            else:
                eix_list2.append(face.Id)

#EixoDisc1
contact = Model.Connections.AddContactRegion()
contact.Activate()
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = [sorteddisc2[0][0]]
contact.TargetLocation = mysel
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = eix_list1
contact.SourceLocation = mysel

#EixoDisc2
contact = Model.Connections.AddContactRegion()
contact.Activate()
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = [sorteddisc[0][0]]
contact.TargetLocation = mysel
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = eix_list2
contact.SourceLocation = mysel

analysis1 = Model.Analyses[0]
analysis_settings = analysis1.AnalysisSettings

#Cria a Forca

volcarc={}
aux = 0
for body in carc.Bodies:
    if body.Centroid[2]<-0.001:
        volcarc[aux] = body.Volume
    aux +=1
sortedvolcarc = sorted(volcarc.items(),key = lambda item:item[1])
force_id = []
for i in range(0,3):
    if i == 2:
        area = {}
        aux = 0
        for face in carc.Bodies[sortedvolcarc[-1][0]].Faces:
            area[aux] = face.Area
            aux+=1
        sortedarea = sorted(area.items(),key = lambda item:item[1])
        force_id.append(carc.Bodies[sortedvolcarc[-1][0]].Faces[sortedarea[-1][0]].Id)
        area = None
    else:
        area = {}
        aux = 0
        for face in carc.Bodies[sortedvolcarc[i][0]].Faces:
            area[aux] = face.Area
            aux+=1
        sortedarea = sorted(area.items(),key = lambda item:item[1])
        force_id.append(carc.Bodies[sortedvolcarc[i][0]].Faces[sortedarea[-1][0]].Id)
        area = None
force = analysis1.AddRemoteForce()
force.DefineBy = LoadDefineBy.Components
force.ZComponent.Output.DiscreteValues =[Quantity(str(carga)+'.0 [N]')]
force.ZCoordinate = Quantity('-'+str(DT/2)+'.0 [mm]')
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = force_id
force.Location = mysel

#Cria os RemDisp
for body in eixo.Bodies:
    print(abs(body.Centroid[0]) - DistEManc/2*1e-3)
    if abs(abs(body.Centroid[0]) - DistEManc/2*1e-3)<=0.005:
        print(body.Id)
        for face in body.Faces:
            if abs(abs(face.Centroid[0])-abs(body.Centroid[0]))<=0.0001:
                rem_disp = analysis1.AddRemoteDisplacement()
                rem_disp.ZComponent.Output.DiscreteValues = [Quantity('0 [mm]')]
                rem_disp.YComponent.Output.DiscreteValues = [Quantity('0 [mm]')]
                mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
                mysel.Ids = [face.Id]
                rem_disp.Location = mysel

for body in eixo.Bodies:
    if body.Centroid[0]<-DistEManc/2*1e-3-0.02:
        for face in body.Faces:
            if face.Centroid[0]<body.Centroid[0]-0.01:
                rem_disp = analysis1.AddRemoteDisplacement()
                rem_disp.XComponent.Output.DiscreteValues = [Quantity('0 [mm]')]
                mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
                mysel.Ids = [face.Id]
                rem_disp.Location = mysel


sol = analysis1.Solution

#Create Solution Steps
#Create Eixo Solution
p1eixo = sol.AddMaximumPrincipalStress()
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = eixo_id_list
p1eixo.Location = mysel
p3eixo = sol.AddMinimumPrincipalStress()
p3eixo.Location = mysel

#Create Disco Solution

p1disco = sol.AddMaximumPrincipalStress()
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = [sortedareadisc[-1][0]]
p1disco.Location = mysel
p3disco = sol.AddMinimumPrincipalStress()
p3disco.Location = mysel

#Create Carc Solution

p1carc = sol.AddMaximumPrincipalStress()
mysel = SM.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
mysel.Ids = carc_id_list
p1carc.Location = mysel
p3carc = sol.AddMinimumPrincipalStress()
p3carc.Location = mysel

#Add Moment Reaction

mrec = sol.AddMomentReaction()
mrec.LocationMethod = LocationDefinitionMethod.ContactRegion
mrec.ContactRegionSelection = contact

frec = sol.AddForceReaction()
frec.LocationMethod = LocationDefinitionMethod.ContactRegion
frec.ContactRegionSelection = contact



analysis_settings.NodalForces = OutputControlsNodalForcesType.Yes
analysis1.Solve()

fx = frec.XAxis.ToString().replace('[N]','').replace(' ','').replace('.',',')
fy = frec.YAxis.ToString().replace('[N]','').replace(' ','').replace('.',',')
fz = frec.ZAxis.ToString().replace('[N]','').replace(' ','').replace('.',',')
mx = mrec.XAxis.ToString().replace('[N mm]','').replace(' ','').replace('.',',')
my = mrec.YAxis.ToString().replace('[N mm]','').replace(' ','').replace('.',',')
mz = mrec.ZAxis.ToString().replace('[N mm]','').replace(' ','').replace('.',',')
s1disco = p1disco.Maximum.ToString().replace('[MPa]','').replace(' ','').replace('.',',')
s3disco = p3disco.Minimum.ToString().replace('[MPa]','').replace(' ','').replace('.',',')
s1carc = p1carc.Maximum.ToString().replace('[MPa]','').replace(' ','').replace('.',',')
s3carc = p3carc.Minimum.ToString().replace('[MPa]','').replace(' ','').replace('.',',')
s1eixo = p1eixo.Maximum.ToString().replace('[MPa]','').replace(' ','').replace('.',',')
s3eixo = p3eixo.Minimum.ToString().replace('[MPa]','').replace(' ','').replace('.',',')

f = open(file_path,'w+')
f.write('sep=;\n')
f.write('Fx;Fy;Fz;Mx;My;Mz;S1DISCO;S3DISCO;S1CARC;S3CARC;S1EIXO;S3EIXO\n')
f.write(fx+";"+fy+";"+fz+";"+mx+";"+my+";"+mz+";"+s1disco+";"+s3disco+";"+s1carc+";"+s3carc+";"+s1eixo+";"+s3eixo)
f.close()


