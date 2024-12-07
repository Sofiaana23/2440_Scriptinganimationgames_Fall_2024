import maya.cmds as cmds

class AssignColor(object):
    colorSelector = ''

    def __init__(self, shortName="", widthHeight=(400,200)):
        self.title="Color Assignment"
        self.shortName=shortName
        self.widthHeight=widthHeight
    
    def SpawnWindow(self):
        window = cmds.window( title=self.title, iconName=self.shortName, widthHeight=self.widthHeight)
        cmds.columnLayout( adjustableColumn=True )
        cmds.text("Select Color")
        self.colorSelector = cmds.colorInputWidgetGrp( label='Color', rgb=(1, 0, 0) )
        cmds.button("Assign Color", command=lambda x: self.setColor())
        cmds.showWindow(window)

    def GetColor(self):
        return cmds.colorInputWidgetGrp(self.colorSelector, query=True, rgb=True)

    def getShapes(self, selection):
        # update selection to only the shapes
        cmds.select(selection, hierarchy=True, replace=True)
        return cmds.ls(selection=True, shapes=True)


    def setColor(self):
        color = self.GetColor()
        selection = cmds.ls(selection=True)
        newSelection = self.getShapes(selection)
        for shape in newSelection:
            cmds.setAttr(f"{shape}.overrideEnabled", True)
            cmds.setAttr(f"{shape}.overrideRGBColors", True)
            cmds.setAttr(f"{shape}.overrideColorRGB", color[0],color[1],color[2], type='double3')
        
        # reset selection to original objects
        cmds.select(selection, replace=True)

# To Execute in Maya, the following commands must be run in the Command Window:
# import AssignColor
# AssignColor.AssignColor().SpawnWindow()