import maya.cmds as cmds

def rename(pattern):

    segments = pattern.split("_")
    if len(segments) != 3:
        print("The naming convention for this pattern must be 'Name_##_NodeType'")
        return
    if len(segments[1]) < 2:
        print("The minimum length for the number segment is 2 characters")
        return
    
    # Starting index value
    index = 1

    selection = cmds.ls(selection=True)
    for object in selection:
        paddingFormatCharacter=f"0{len(segments[1])}"
        updatedName = f"{segments[0]}_{format(index, paddingFormatCharacter)}_{segments[2]}"
        cmds.rename(object, updatedName)
        index += 1

rename("renamed_###_object")