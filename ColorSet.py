import maya.cmds as cmds

def getShapes(selection):
    # update selection to only the shapes
    cmds.select(selection, hierarchy=True, replace=True)
    return cmds.ls(selection=True, shapes=True)


def setColor(colorID):
    selection = cmds.ls(selection=True)
    newSelection = getShapes(selection)
    for shape in newSelection:
        cmds.setAttr(f"{shape}.overrideEnabled", True)
        cmds.setAttr(f"{shape}.overrideColor", colorID)
    
    # reset selection to original objects
    cmds.select(selection, replace=True)

setColor(1)