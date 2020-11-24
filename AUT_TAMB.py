import sys
import win32com.client
from win32com.client import gencache
from win32com.client import constants
import os
import time

try:
	arg_list = str(sys.argv)
	dt = str(sys.argv[1])
	lt = str(sys.argv[2])
	dm = str(sys.argv[3])
	anel = str(sys.argv[4])
	tamanho = str(sys.argv[5])
	material = str(sys.argv[6])
	ecar = str(sys.argv[7])
	edl = str(sys.argv[8])
	deixo = str(sys.argv[9])
	angltrans = str(sys.argv[10])
	carga = str(sys.argv[11])
	dpe = str(sys.argv[12])
	anglpe = str(sys.argv[13])
	save_path = str(sys.argv[14])
except:
	dt = 650
	lt = 1600
	dm = 2110
	anel = 7012
	tamanho = "170x225"
	material = 300
	ecar = 16
	edl = 25
	deixo = "160 "
	angltrans = 20
	carga = 50000
	dpe = 0
	anglpe = 20
	save_path = "C:\\STEP.stp"

class Inventor():

    def __init__(self):
        self.oApp = win32com.client.Dispatch('Inventor.Application')
        mod = gencache.EnsureModule('{D98A091D-3A0F-4C3E-B36E-61F62068D488}', 0, 1, 0)
        self.oApp = mod.Application(self.oApp)

    def Cast(self,var,cast):
        var = win32com.client.CastTo(var,cast)
        return var

    def file_open(self,file_path):
        oDoc = self.oApp.Documents.Open(file_path)
        self.oDoc = oDoc
        return oDoc
    
    def open_excel(self):
        oLef = self.oDoc.ReferencedOLEFileDescriptors(1)
        oLef = self.Cast(oLef,'ReferencedOLEFileDescriptor')
        xlApp = win32com.client.gencache.EnsureDispatch("Excel.Application")
        
        oLef.Activate(constants.kEditOpenOLEVerb, oLef)
        oWb = xlApp.ActiveWorkbook
        self.oWb = oWb
        return oWb
        #oWb = self.Cast(oWb,'Workbook')

    def change_param(self,rang,param):
        self.oWb.ActiveSheet.Range(rang).Value = param
    
    def save_excel(self,file_path):
        self.oWb.Save()
        self.oWb.SaveCopyAs(file_path)
        self.oWb.Close()
        self.oWb = None

    def update(self):
    	self.oDoc.Update()
    	self.oDoc.Save()
    	#self.oDoc.Close()
    	self.oDoc = None

    def export(self,file_path):
    	self.oDoc.Update()
    	self.oDoc.Save()
    	self.export_step(file_path)
    	#self.oDoc.Close()
    	self.oDoc = None

    def export_step(self,file_path):
        oSTEPTranslator = self.oApp.ApplicationAddIns.ItemById("{90AF7F40-0C01-11D5-8E83-0010B541CD80}")
        oContext = self.oApp.TransientObjects.CreateTranslationContext()
        oOptions =self.oApp.TransientObjects.CreateNameValueMap()
        oContext.Type = constants.kFileBrowseIOMechanism
        oData = self.oApp.TransientObjects.CreateDataMedium()
        oData.FileName = file_path
        oSTEPTranslator = self.Cast(oSTEPTranslator,'TranslatorAddIn')
        oSTEPTranslator.SaveCopyAs(self.oApp.ActiveDocument,oContext,oOptions,oData)


if __name__ == '__main__':
	invApp=Inventor()
	invApp.oApp.Visible=True
	invApp.oApp.SilentOperation=True
	dir_path = 'C:\\Users\\gabriel.prado\\Desktop\\SINTEC_TAMB\\'
	esq_path = 'Simulacao-Tambor_ Esqueleto.ipt'
	conj_path = 'Simulacao-Tambor_ Tambor.iam'
	esq = invApp.file_open(dir_path+esq_path)
	invApp.open_excel()
	invApp.change_param(rang='B9',param=int(dt))
	invApp.change_param(rang='B10',param=int(lt))
	invApp.change_param(rang='B11',param=int(dm))
	invApp.change_param(rang='B12',param=anel)
	invApp.change_param(rang='B13',param=tamanho)
	invApp.change_param(rang='B14',param=int(material))
	invApp.change_param(rang='B15',param=int(ecar))
	invApp.change_param(rang='B16',param=int(edl))
	invApp.change_param(rang='B19',param=str("Eixo "+str(int(deixo))+" - Mancal SNL"))
	invApp.change_param(rang='B21',param=int(angltrans))
	invApp.change_param(rang='B22',param=int(dpe))
	invApp.change_param(rang='B24',param=int(anglpe))
	invApp.save_excel(save_path.replace('.stp','.xlsx'))
	invApp.update()
	file = invApp.file_open(dir_path + conj_path)
	invApp.oApp.SilentOperation=True
	invApp.export(save_path)
	invApp.Quit()


