import maya.cmds as cmds

def main():

    # 1. Get Selected Elements from Current Maya Session
    selected = cmds.ls(selection=True)

    # Iterate over Each Element individually to make groups for each selected element
    for object in selected:
        # 2. Create Empty Group
        # 5. Set name to be {object name}_Grp
        new_group = cmds.group(empty=True, name=f"{object}_Grp")

        # 3. Set Group positional and rotational data to match the child object
        attributes = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ']
        for attribute in attributes:
            cmds.setAttr(f"{new_group}.{attribute}", cmds.getAttr(f"{object}.{attribute}"))
        
        # 4. Parent Selected Objects into new Group
        cmds.parent(object, new_group)


if __name__=="__main__":
    main()