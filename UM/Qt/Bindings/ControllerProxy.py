from PyQt5.QtCore import QObject, QCoreApplication, pyqtSlot, QUrl

from UM.Application import Application
from UM.Scene.SceneNode import SceneNode
from UM.Scene.BoxRenderer import BoxRenderer
from UM.Operations.AddSceneNodeOperation import AddSceneNodeOperation
from UM.Scene.Selection import Selection
from UM.Operations.RemoveSceneNodesOperation import RemoveSceneNodesOperation
from UM.LoadWorkspaceJob import LoadWorkspaceJob

import os.path

class ControllerProxy(QObject):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._controller = Application.getInstance().getController()

    @pyqtSlot(str)
    def setActiveView(self, view):
        self._controller.setActiveView(view)

    @pyqtSlot(str)
    def setActiveTool(self, tool):
        self._controller.setActiveTool(tool)

    @pyqtSlot()
    def removeSelection(self):
        if not Selection.hasSelection():
            return

        op = RemoveSceneNodesOperation(Selection.getAllSelectedObjects())
        op.push()
        Selection.clear()

    @pyqtSlot()
    def saveWorkspace(self):
        #self.loadWorkSpace() # DEBUG STUFF
        print("fhfhfhfh")
        Application.getInstance().getWorkspaceFileHandler().write("derp.mlp",Application.getInstance().getStorageDevice('local'))
        pass #TODO: Implement workspace saving

    @pyqtSlot()
    def loadWorkSpace(self):
        job = LoadWorkspaceJob("meshlab.mlp")
        job.finished.connect(self._loadWorkspaceFinished)
        job.start()     
        #TODO: Implement.
        pass
    
    def _loadWorkspaceFinished(self,job):
        node = job.getResult()
        self._controller.getScene().setRoot(node)
