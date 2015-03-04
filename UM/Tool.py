from UM.Signal import Signal, SignalEmitter
from UM.PluginObject import PluginObject

##  Abstract base class for tools that manipulate the scene.
#
class Tool(PluginObject, SignalEmitter):
    def __init__(self):
        super().__init__() # Call super to make multiple inheritence work.
        self._renderer = None
        self._controller = None

    ##  Handle an event.
    #   \param event \type{Event} The event to handle.
    #   \sa Event
    def event(self, event):
        pass

    def getController(self):
        return self._controller

    def setController(self, controller):
        self._controller = controller
