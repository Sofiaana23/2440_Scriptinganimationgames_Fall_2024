import maya.cmds as cmds

def createMainBody():
    cmds.polySphere(radius=5, name="base")
    cmds.move(2.5,moveY=True)
    cmds.polySphere(radius=3.5, name="body")
    cmds.move(8,moveY=True)
    cmds.polySphere(radius=2, name="head")
    cmds.move(12.5, moveY=True)

def createButtons():
    cmds.polySphere(radius=.25, name="midButton")
    cmds.move(8, 3.5, moveYZ=True)
    cmds.polySphere(radius=.25, name="botButton")
    cmds.move(7, 3.25, moveYZ=True)
    cmds.polySphere(radius=.25, name="topButton")
    cmds.move(9, 3.25, moveYZ=True)

def createFace():
    cmds.polySphere(radius=.25, name="leftEye")
    cmds.move(-.5, 13.5, 1.65)
    cmds.polySphere(radius=.25, name="rightEye")
    cmds.move(.5, 13.5, 1.65)
    cmds.polyCone(radius=.5, height=3, name="nose")
    cmds.rotate(90, rotateX=True)
    cmds.move(13, 2, moveYZ=True)

def createHat():
    cmds.polyCylinder(radius=2, height=.125, name="hatBrim")
    cmds.move(14.25, moveY=True)
    cmds.polyCylinder(radius=1.25, height=3, name="hatBody")
    cmds.move(15.75, moveY=True)

def main():
    createMainBody()
    createButtons()
    createFace()
    createHat()
    pass

if __name__=="__main__":
    main()