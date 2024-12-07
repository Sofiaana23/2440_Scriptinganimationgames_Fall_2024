import maya.cmds as cmds

class SequentialRenamer(object):
    textFieldValue=''
    previewText=''

    def __init__(self, shortName="", widthHeight=(300,100)):
        self.title="Sequential Renamer"
        self.shortName=shortName
        self.widthHeight=widthHeight
        
    def SpawnWindow(self):
        window = cmds.window( title=self.title, iconName=self.shortName, widthHeight=self.widthHeight)
        cmds.columnLayout( adjustableColumn=True )
        cmds.text("Rename Pattern")
        self.textFieldValue = cmds.textField()
        self.previewText = cmds.text("Example Pattern: Node_##_Type")
        cmds.textField(self.textFieldValue, edit=True, textChangedCommand=lambda x: self.SetPreview())
        cmds.button("Rename", command=lambda x: self.rename())
        cmds.showWindow(window)
        
    def GetPattern(self):
        return cmds.textField(self.textFieldValue, query=True, text=True)
    
    def SetPreview(self):
        preview = self.GetPreview()
        cmds.text(self.previewText, edit=True, label=preview)

    def GetPreview(self):
        pattern = self.GetPattern()

        segments = pattern.split("_")
        if len(segments) != 3:
            return("Invalid Pattern: must be 'Name_##_Type'")
        if len(segments[1]) < 2:
            return("Invalid Pattern: Sequence Minimum of 2 Characters")

        paddingFormatCharacter=f"0{len(segments[1])}"
        return f"{segments[0]}_{format(1, paddingFormatCharacter)}_{segments[2]}"

    def rename(self):
        pattern = self.GetPattern()
        segments = pattern.split("_")
        
        if "Invalid Pattern:" in self.GetPreview():
            print("Invalid Pattern")
            return
        
        segments = pattern.split("_")
        # Starting index value
        index = 1

        selection = cmds.ls(selection=True)
        for object in selection:
            paddingFormatCharacter=f"0{len(segments[1])}"
            updatedName = f"{segments[0]}_{format(index, paddingFormatCharacter)}_{segments[2]}"
            cmds.rename(object, updatedName)
            index += 1

# To Execute in Maya, the following commands must be run in the Command Window:
# import SequentialRenamer
# SequentialRenamer.SequentialRenamer().SpawnWindow()