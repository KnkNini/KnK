# Multi wrap

import maya.mel as mel

body = 'RIG:msh_body'
mshs = mc.ls(sl=True)

for msh in mshs:
    mc.select(msh)    
    mc.select(body, add=True)
    mel.eval('doWrapArgList("7", {"1", ".0", "1.0", "2", "0", "1", "0", "0"});')


