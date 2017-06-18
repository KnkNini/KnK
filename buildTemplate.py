import maya.cmds as mc
import maya.mel as mel

def buildTemplate():
    for x in mc.ls(sl=True, type='transform'):
        tpls = []
        if x not in mc.ls('tpl_*'):
            mc.warning("must start with 'tpl_', please rename", x)
            return ("must start with 'tpl_', please rename", x)
        else:
            tpls.append(x)

        tplPosT = mc.xform(x, q=True, translation=True, worldSpace=True)
        tplPosR = mc.xform(x, q=True, rotation=True, worldSpace=True)
        objName = x.split('tpl_')[1]

        grp = mc.group(mc.group(em=True, n=('c_' + objName)), n=('root_' + objName))
        root = 'root_' + objName
        sk = mc.joint(n=('sk_' + objName))
        mc.parent(sk, 'c_' + objName)
        mc.setAttr(root + ".translate", tplPosT[0], tplPosT[1], tplPosT[2])
        mc.setAttr(root + ".rotate", tplPosR[0], tplPosR[1], tplPosR[2])
        if not mc.getAttr(sk + '.translate') == (0, 0, 0):
            mc.setAttr(sk + ".translate", 0, 0, 0)
        elif not mc.getAttr(sk + ".rotate") == (0, 0, 0):
            mc.setAttr(sk + ".rotate", 0, 0, 0)
        mc.delete(x)

buildTemplate()