import maya.cmds as mc

def checkTumble():
    if mc.tumbleCtx('tumbleContext', query=True, localTumble=1) == False:
        mc.tumbleCtx('tumbleContext', edit=True, localTumble=1)
    else:
        mc.warning("Tumble already about Center of Interest")

checkTumble()