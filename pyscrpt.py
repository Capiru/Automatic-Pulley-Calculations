DistEManc = 2080
LargMancal = 80
file_path = "C:\Users\gabriel.prado\Desktop\AUT_TAMB_WV\STEP.stp"
# Python Script, API Version = V18

# Open File
importOptions = ImportOptions.Create()
DocumentOpen.Execute(file_path, importOptions, GetMaps("e6ebd312"))
# EndBlock


# Create Datum Plane
selection = Selection.Create(GetRootPart().Components[1].Content.Bodies[2].Faces[4])
result = DatumPlaneCreator.Create(selection, False, None)
# EndBlock

# Move Upto Selected Object
selection = Selection.Create(GetRootPart().DatumPlanes[0])
upToSelection = Selection.Create(GetRootPart().Components[0].Components[0].Content.Bodies[0].Edges[11])
moveFrame = Move.CreateFrame(selection)
axis = HandleAxis.Z
options = MoveOptions()
options.CreatePatterns = False
options.DetachFirst = False
options.MaintainOrientation = False
options.MaintainMirrorRelationships = True
options.MaintainConnectivity = True
options.MaintainOffsetRelationships = True
options.Copy = False
result = Move.UpTo(selection, upToSelection, moveFrame, axis, options)
# EndBlock

# Create Datum Plane
selection = Selection.Create(GetRootPart().DatumPlanes[0])
result = DatumPlaneCreator.Create(selection, False, None)
# EndBlock

# Create Datum Plane
selection = Selection.Create(GetRootPart().DatumPlanes[0])
result = DatumPlaneCreator.Create(selection, False, None)
# EndBlock

# Create Datum Plane
selection = Selection.Create(GetRootPart().DatumPlanes[0])
result = DatumPlaneCreator.Create(selection, False, None)
# EndBlock

# Translate Along Z Handle
selection = Selection.Create(GetRootPart().DatumPlanes[0])
direction = Move.GetDirection(selection)
options = MoveOptions()
options.CreatePatterns = False
options.DetachFirst = False
options.MaintainOrientation = False
options.MaintainMirrorRelationships = True
options.MaintainConnectivity = True
options.MaintainOffsetRelationships = True
options.Copy = False
result = Move.Translate(selection, direction, MM(DistEManc/2-LargMancal/2), options)
# EndBlock


# Translate Along Z Handle
selection = Selection.Create(GetRootPart().DatumPlanes[1])
direction = Move.GetDirection(selection)
options = MoveOptions()
options.CreatePatterns = False
options.DetachFirst = False
options.MaintainOrientation = False
options.MaintainMirrorRelationships = True
options.MaintainConnectivity = True
options.MaintainOffsetRelationships = True
options.Copy = False
result = Move.Translate(selection, direction, MM(DistEManc/2+LargMancal/2), options)
# EndBlock

# Translate Along Z Handle
selection = Selection.Create(GetRootPart().DatumPlanes[2])
direction = Move.GetDirection(selection)
options = MoveOptions()
options.CreatePatterns = False
options.DetachFirst = False
options.MaintainOrientation = False
options.MaintainMirrorRelationships = True
options.MaintainConnectivity = True
options.MaintainOffsetRelationships = True
options.Copy = False
result = Move.Translate(selection, direction, MM(-DistEManc/2+LargMancal/2), options)
# EndBlock

# Translate Along Z Handle
selection = Selection.Create(GetRootPart().DatumPlanes[3])
direction = Move.GetDirection(selection)
options = MoveOptions()
options.CreatePatterns = False
options.DetachFirst = False
options.MaintainOrientation = False
options.MaintainMirrorRelationships = True
options.MaintainConnectivity = True
options.MaintainOffsetRelationships = True
options.Copy = False
result = Move.Translate(selection, direction, MM(-DistEManc/2-LargMancal/2), options)
# EndBlock


# Slice Bodies by Plane
selection = Selection.Create(GetRootPart().Components[1].Content.Bodies[2])
datum = Selection.Create(GetRootPart().DatumPlanes[0])
result = SplitBody.ByCutter(selection, datum)
# EndBlock

# Slice Bodies by Plane
selection = Selection.Create([GetRootPart().Components[1].Content.Bodies[2],
    GetRootPart().Components[1].Content.Bodies[7]])
datum = Selection.Create(GetRootPart().DatumPlanes[1])
result = SplitBody.ByCutter(selection, datum)
# EndBlock

# Slice Bodies by Plane
selection = Selection.Create(GetRootPart().Components[1].Content.Bodies[1])
datum = Selection.Create(GetRootPart().DatumPlanes[2])
result = SplitBody.ByCutter(selection, datum)
# EndBlock

# Slice Bodies by Plane
selection = Selection.Create([GetRootPart().Components[1].Content.Bodies[1],
    GetRootPart().Components[1].Content.Bodies[9]])
datum = Selection.Create(GetRootPart().DatumPlanes[3])
result = SplitBody.ByCutter(selection, datum)
# EndBlock


# Create Datum Plane
selection = Selection.Create(GetRootPart().Components[0].Components[1].Content.Bodies[0].Faces[2])
result = DatumPlaneCreator.Create(selection, True, None)
# EndBlock

# Create Datum Plane
selection = Selection.Create(GetRootPart().Components[0].Components[1].Content.Bodies[0].Faces[6])
result = DatumPlaneCreator.Create(selection, True, None)
# EndBlock

# Create Datum Plane
selection = Selection.Create(GetRootPart().Components[0].Components[2].Content.Bodies[0].Faces[2])
result = DatumPlaneCreator.Create(selection, True, None)
# EndBlock

# Create Datum Plane
selection = Selection.Create(GetRootPart().Components[0].Components[2].Content.Bodies[0].Faces[6])
result = DatumPlaneCreator.Create(selection, True, None)
# EndBlock

# Slice Bodies by Plane
selection = Selection.Create([GetRootPart().Components[0].Components[0].Content.Bodies[0],
    GetRootPart().Components[0].Components[0].Content.Bodies[1]])
datum = Selection.Create(GetRootPart().DatumPlanes[6])
result = SplitBody.ByCutter(selection, datum)
# EndBlock

# Slice Bodies by Plane
selection = Selection.Create([GetRootPart().Components[0].Components[0].Content.Bodies[0],
    GetRootPart().Components[0].Components[0].Content.Bodies[1],
    GetRootPart().Components[0].Components[0].Content.Bodies[2],
    GetRootPart().Components[0].Components[0].Content.Bodies[3]])
datum = Selection.Create(GetRootPart().DatumPlanes[7])
result = SplitBody.ByCutter(selection, datum)
# EndBlock

# Slice Bodies by Plane
selection = Selection.Create([GetRootPart().Components[0].Components[0].Content.Bodies[0],
    GetRootPart().Components[0].Components[0].Content.Bodies[1],
    GetRootPart().Components[0].Components[0].Content.Bodies[2],
    GetRootPart().Components[0].Components[0].Content.Bodies[3],
    GetRootPart().Components[0].Components[0].Content.Bodies[4],
    GetRootPart().Components[0].Components[0].Content.Bodies[5]])
datum = Selection.Create(GetRootPart().DatumPlanes[5])
result = SplitBody.ByCutter(selection, datum)
# EndBlock

# Slice Bodies by Plane
selection = Selection.Create([GetRootPart().Components[0].Components[0].Content.Bodies[0],
    GetRootPart().Components[0].Components[0].Content.Bodies[1],
    GetRootPart().Components[0].Components[0].Content.Bodies[2],
    GetRootPart().Components[0].Components[0].Content.Bodies[3],
    GetRootPart().Components[0].Components[0].Content.Bodies[4],
    GetRootPart().Components[0].Components[0].Content.Bodies[5],
    GetRootPart().Components[0].Components[0].Content.Bodies[6],
    GetRootPart().Components[0].Components[0].Content.Bodies[7]])
datum = Selection.Create(GetRootPart().DatumPlanes[4])
result = SplitBody.ByCutter(selection, datum)
# EndBlock

# Delete Selection
selection = Selection.Create(GetRootPart().Components[0].Components[3].Content.Bodies[0])
result = Delete.Execute(selection)
# EndBlock

# Make Components
selection = Selection.Create([GetRootPart().Components[0].Components[0].Content.Bodies[6],
    GetRootPart().Components[0].Components[0].Content.Bodies[7],
    GetRootPart().Components[0].Components[0].Content.Bodies[0],
    GetRootPart().Components[0].Components[0].Content.Bodies[1],
    GetRootPart().Components[0].Components[0].Content.Bodies[2],
    GetRootPart().Components[0].Components[0].Content.Bodies[3],
    GetRootPart().Components[0].Components[0].Content.Bodies[4],
    GetRootPart().Components[0].Components[0].Content.Bodies[5],
    GetRootPart().Components[0].Components[0].Content.Bodies[9],
    GetRootPart().Components[0].Components[0].Content.Bodies[8]])
result = ComponentHelper.MoveBodiesToComponent(selection, None)
# EndBlock

# Rename 'Component1' to 'CARCACA'
# Record Failed
# EndBlock

# Change Object Visibility
selection = Selection.Create([GetRootPart().Components[3].Content.Bodies[0],
    GetRootPart().Components[3].Content.Bodies[1],
    GetRootPart().Components[3].Content.Bodies[2],
    GetRootPart().Components[3].Content.Bodies[3],
    GetRootPart().Components[3].Content.Bodies[4],
    GetRootPart().Components[3].Content.Bodies[5],
    GetRootPart().Components[3].Content.Bodies[6],
    GetRootPart().Components[3].Content.Bodies[7],
    GetRootPart().Components[3].Content.Bodies[8],
    GetRootPart().Components[3].Content.Bodies[9]])
visibility = VisibilityType.Hide
inSelectedView = False
faceLevel = False
ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
# EndBlock

# Slice Body by Faces
selection = Selection.Create(GetRootPart().Components[0].Components[1].Content.Bodies[0])
toolFaces = Selection.Create(GetRootPart().Components[0].Components[1].Content.Bodies[0].Faces[6])
result = SplitBody.ByCutter(selection, toolFaces, True)
# EndBlock

# Delete Objects
selection = Selection.Create(GetRootPart().Components[0].Components[1].Content.Bodies[2])
result = Combine.RemoveRegions(selection)
# EndBlock

# Slice Body by Faces
selection = Selection.Create(GetRootPart().Components[0].Components[2].Content.Bodies[0])
toolFaces = Selection.Create(GetRootPart().Components[0].Components[2].Content.Bodies[0].Faces[6])
result = SplitBody.ByCutter(selection, toolFaces, True)
# EndBlock

# Delete Objects
selection = Selection.Create(GetRootPart().Components[0].Components[2].Content.Bodies[2])
result = Combine.RemoveRegions(selection)
# EndBlock

# Merge Bodies
targets = Selection.Create([GetRootPart().Components[0].Components[2].Content.Bodies[0],
    GetRootPart().Components[0].Components[2].Content.Bodies[1]])
result = Combine.Merge(targets)
# EndBlock

# Merge Bodies
targets = Selection.Create([GetRootPart().Components[0].Components[1].Content.Bodies[1],
    GetRootPart().Components[0].Components[1].Content.Bodies[0]])
result = Combine.Merge(targets)
# EndBlock

# Merge Bodies
targets = Selection.Create([GetRootPart().Components[0].Components[1].Content.Bodies[0],
    GetRootPart().Components[0].Components[3].Content.Bodies[0]])
result = Combine.Merge(targets)
# EndBlock

# Delete Selection
selection = Selection.Create(GetRootPart().Components[2].Content.Bodies[0])
result = Delete.Execute(selection)
# EndBlock

# Delete Selection
selection = Selection.Create(GetRootPart().Components[2].Content.Bodies[0])
result = Delete.Execute(selection)
# EndBlock

# Delete Selection
selection = Selection.Create(GetRootPart().Components[0].Components[3].Content.Bodies[0])
result = Delete.Execute(selection)
# EndBlock

# Make Components
selection = Selection.Create([GetRootPart().Components[0].Components[1].Content.Bodies[0],
    GetRootPart().Components[0].Components[2].Content.Bodies[0]])
result = ComponentHelper.MoveBodiesToComponent(selection, None)
# EndBlock

# Rename 'Component1' to 'DISCO'
# Record Failed
# EndBlock

# Change Object Visibility
selection = Selection.Create([GetRootPart().Components[4].Content.Bodies[0],
    GetRootPart().Components[4].Content.Bodies[1]])
visibility = VisibilityType.Hide
inSelectedView = False
faceLevel = False
ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
# EndBlock

# Delete Selection
selection = Selection.Create(GetRootPart().Components[2].Content.Bodies[0].Faces[0])
result = Delete.Execute(selection)
# EndBlock

# Delete Selection
selection = Selection.Create(GetRootPart().Components[0].Components[3].Content.Bodies[0].Faces[0])
result = Delete.Execute(selection)
# EndBlock

# Make Components
selection = Selection.Create([GetRootPart().Components[1].Content.Bodies[0],
    GetRootPart().Components[1].Content.Bodies[1],
    GetRootPart().Components[1].Content.Bodies[2],
    GetRootPart().Components[1].Content.Bodies[3],
    GetRootPart().Components[1].Content.Bodies[4],
    GetRootPart().Components[1].Content.Bodies[5],
    GetRootPart().Components[1].Content.Bodies[6],
    GetRootPart().Components[1].Content.Bodies[7],
    GetRootPart().Components[1].Content.Bodies[8],
    GetRootPart().Components[1].Content.Bodies[9],
    GetRootPart().Components[1].Content.Bodies[10]])
result = ComponentHelper.MoveBodiesToComponent(selection, None)
# EndBlock

# Rename 'Component1' to 'EIXO'
# Record Failed
# EndBlock

# Change Object Visibility
selection = Selection.Create([GetRootPart().Components[5].Content.Bodies[0],
    GetRootPart().Components[5].Content.Bodies[1],
    GetRootPart().Components[5].Content.Bodies[2],
    GetRootPart().Components[5].Content.Bodies[3],
    GetRootPart().Components[5].Content.Bodies[4],
    GetRootPart().Components[5].Content.Bodies[5],
    GetRootPart().Components[5].Content.Bodies[6],
    GetRootPart().Components[5].Content.Bodies[7],
    GetRootPart().Components[5].Content.Bodies[8],
    GetRootPart().Components[5].Content.Bodies[9],
    GetRootPart().Components[5].Content.Bodies[10]])
visibility = VisibilityType.Hide
inSelectedView = False
faceLevel = False
ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
# EndBlock

# Delete Empty Components
selection = Selection.Create(GetRootPart())
ComponentHelper.DeleteEmptyComponents(selection, None)
# EndBlock

# Change Object Visibility
selection = Selection.Create([GetRootPart().Components[2].Content.Bodies[0],
    GetRootPart().Components[2].Content.Bodies[1],
    GetRootPart().Components[2].Content.Bodies[2],
    GetRootPart().Components[2].Content.Bodies[3],
    GetRootPart().Components[2].Content.Bodies[4],
    GetRootPart().Components[2].Content.Bodies[5],
    GetRootPart().Components[2].Content.Bodies[6],
    GetRootPart().Components[2].Content.Bodies[7],
    GetRootPart().Components[2].Content.Bodies[8],
    GetRootPart().Components[2].Content.Bodies[9],
    GetRootPart().Components[2].Content.Bodies[10]])
visibility = VisibilityType.Show
inSelectedView = False
faceLevel = False
ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
# EndBlock

# Change Object Visibility
selection = Selection.Create([GetRootPart().Components[1].Content.Bodies[0],
    GetRootPart().Components[1].Content.Bodies[1]])
visibility = VisibilityType.Show
inSelectedView = False
faceLevel = False
ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
# EndBlock

# Change Object Visibility
selection = Selection.Create([GetRootPart().Components[0].Content.Bodies[0],
    GetRootPart().Components[0].Content.Bodies[1],
    GetRootPart().Components[0].Content.Bodies[2],
    GetRootPart().Components[0].Content.Bodies[3],
    GetRootPart().Components[0].Content.Bodies[4],
    GetRootPart().Components[0].Content.Bodies[5],
    GetRootPart().Components[0].Content.Bodies[6],
    GetRootPart().Components[0].Content.Bodies[7],
    GetRootPart().Components[0].Content.Bodies[8],
    GetRootPart().Components[0].Content.Bodies[9]])
visibility = VisibilityType.Show
inSelectedView = False
faceLevel = False
ViewHelper.SetObjectVisibility(selection, visibility, inSelectedView, faceLevel)
# EndBlock

# Share Topology
options = ShareTopologyOptions()
options.Tolerance = MM(0.2)
options.PreserveInstances = True
result = ShareTopology.FindAndFix(options)
# EndBlock

a= ComponentHelper.SetName(GetRootPart().Components[0],'CARC')

a= ComponentHelper.SetName(GetRootPart().Components[1],'DISCO')

a= ComponentHelper.SetName(GetRootPart().Components[2],'EIXO')

# Save File
options = ExportOptions.Create()
DocumentSave.Execute(file_path.replace(".stp",".scdoc"), options)
# EndBlock