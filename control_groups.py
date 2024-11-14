import maya.cmds as cmds

def createGroup(object):
    # 3a. Create Empty Group & Set Name
    new_group = cmds.group(empty=True, name=getGroupName(object))

    # 3b. Set Group positional and rotational data to match the child object
    copyTransforms(object, new_group)
    
    # 3c. Parent Object into new Group
    cmds.parent(object, new_group)

def copyTransforms(fromObj, toObj):
    desiredRotation = cmds.xform(fromObj, worldSpace=True, rotation=True, q=True)
    desiredTranslation = cmds.xform(fromObj, worldSpace=True, translation=True, q=True)
    cmds.xform(toObj, rotation=desiredRotation, translation=desiredTranslation)

def getControlName(object):
    return stripSuffix(object)+"_Ctrl"

def getGroupName(object):
    return stripSuffix(object)+"_Grp"

def stripSuffix(object):
    result = object
    if result.endswith('_Geo') or result.endswith('_Jnt'):
        return result[:-4]
    return result

def createControl(object):
    # 2a. Create circle
    circle = cmds.circle(name=getControlName(object), nr=[1,0,0])

    control = circle[0]
    # 2b. Translate and Rotate
    copyTransforms(object, control)
    return control

    
def main():

    # 1. Get Selected Elements from Current Maya Session
    selected = cmds.ls(selection=True)

    # Iterate over Each Element individually to make groups for each selected element
    for object in selected:
        # 2. Create control out a NURBS circle
        control = createControl(object)

        # 3. Create parent group for each control
        createGroup(control)


if __name__=="__main__":
    main()