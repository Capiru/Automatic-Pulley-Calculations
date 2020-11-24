import sys
import win32com.client
from win32com.client import gencache
from win32com.client import constants
import os
import time

try:
	arg_list = str(sys.argv)
	directory_assemblies = str(sys.argv[1])

except:
	directory_assemblies = ''

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
	from os import listdir
	from os.path import isfile, join
	onlyfiles = [f for f in listdir(directory_assemblies) if isfile(join(directory_assemblies, f))]
	invApp=Inventor()
	invApp.oApp.Visible=True
	invApp.oApp.SilentOperation=True
	for file in onlyfiles:
		f = invApp.file_open(directory_assemblies+file)
		invApp.export(directory_assemblies+file.replace('.iam','.stp'))
	invApp.Quit()


