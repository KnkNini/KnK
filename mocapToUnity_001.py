## MocapToUnity_v1.1 ##

import os
import sys
import os.path
import maya.cmds as mc
import maya.mel as mel
from pymel import core
from os import listdir
from maya import OpenMayaUI as omui
try:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from shiboken2 import wrapInstance
    print 'Using PySide2'
except:
    from PySide.QtGui import *
    from PySide.QtCore import *
    from shiboken import wrapInstance
    print 'Using PySide'

ptr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(ptr), QtWidgets.QWidget)

class mocapToUnity(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setParent(mayaMainWindow)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("mocapToUnity")
        self.setMinimumWidth(300)
        self.setMinimumHeight(200)
        
        self.openFbxLbl = QLabel(self)
        self.openFbxLbl.setText("Choose .fbx file to import:")
        
        self.openFbxBtn = QPushButton()
        self.openFbxBtn.setText("Select")
        self.openFbxBtn.clicked.connect(self.importFbx)

        self.fbxPathLbl = QLabel(self)
        self.fbxPathLbl.setText("...")
        
        self.selectCrvsLbl = QLabel(self)
        self.selectCrvsLbl.setText("Select anim curves to clean manually or All:")

        self.selCrvsBtn = QPushButton()
        self.selCrvsBtn.setText("Selected")
        self.selCrvsBtn.clicked.connect(self.test)

        self.allCrvsBtn = QPushButton()
        self.allCrvsBtn.setText("All")
        self.allCrvsBtn.clicked.connect(self.test)

        #qle

        self.cleanFbxBtn = QPushButton()
        self.cleanFbxBtn.setText("Clean Fbx")
        self.cleanFbxBtn.clicked.connect(self.cleanFbx)
        
        self.layout = QGridLayout(self)
        
        self.layout.addWidget(self.openFbxLbl, 0, 1)
        self.layout.addWidget(self.openFbxBtn, 1, 1, 1, 2)
        self.layout.addWidget(self.fbxPathLbl, 2, 1, 1, 2)
        self.layout.addWidget(self.selectCrvsLbl, 3, 1, 1, 2)
        self.layout.addWidget(self.selCrvsBtn, 4, 1)
        self.layout.addWidget(self.allCrvsBtn, 4, 2)
        #qle
        self.layout.addWidget(self.cleanFbxBtn, 6, 1, 1, 2)
   
    def test(self):
        print 'toto'
        
    def selectDir(self):
        basicFilter = "FBX Files (*.fbx)"
        #to do: check if file already in qlstDefFold
        myDir = mc.fileDialog2(fileFilter=basicFilter, dialogStyle=2, fm=1)
        self.fbxPathLbl.setText(myDir[0])
        fileEndings = ('.fbx')
        for f in myDir:
            if not f.startswith('.'):
                if not f.endswith(fileEndings):
                    mc.warning("Select a .fbx file")
        return myDir

    def importFbx(self, *args):
        fbx = self.selectDir()
        mc.file(fbx, i=True)

    def cleanFbx(self):
        #selCrvs = self.getSelCurves()
        #crvs = self.getAllCurves()
        #self.snapKeys()
        #self.simplifyCrvs(type=dense, time=0.2, value=0.2)(change qle)
        #self.snapKeys()
        #self.bakeChannel(*unsnapKeys)
        print 'cleanFbx'

    def getAllCrvs(self):
        print "all curves"
    
    def getSelCrvs(self):
        print "selected curves"

if __name__ == "__main__":
    import sys 
    ui = mocapToUnity()
    if (mc.window("mocapToUnity", q=True, exists=True)):
        mc.deleteUI(ui)
        mel.eval('print("Window exists, updating...")')
        ui.show()
    else:
        ui.show()
