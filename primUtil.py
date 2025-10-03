import maya.cmds as cmds

def createPrim(prim, name=None):
    if prim == 'cone':
        obj = cmds.polyCone()[0]
    elif prim == 'cube':
        obj = cmds.polyCube()[0]
    elif prim == 'sphere':
        obj = cmds.polySphere()[0]
    elif prim == 'torus':
        obj = cmds.polyTorus()[0]
    else:
        return None
        
    if not name or name.strip() == "":
        base = prim.lower()
    else:
        base = name.strip()

        if base.endswith("_geo"):
            base = base[:-4]

    index = 1
    while True:
        candidate = "{}{:04d}_geo".format(base, index)
        if not cmds.objExists(candidate):
            new_name = candidate
            break
        index += 1

    obj = cmds.rename(obj, new_name)
    print("Created:", obj)
    return obj