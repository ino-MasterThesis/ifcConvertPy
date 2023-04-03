import os
import subprocess

import ifcopenshell

from util import util

# ===============
# Export gLTF
# ===============


def create_geom(schema, element):

    tmp_ifc = ifcopenshell.file(schema=schema)
    tmp_ifc.add(element)
    dist_ifc = f"../../dist/ifc/{element.GlobalId}.ifc"
    tmp_ifc = removeBBox(tmp_ifc)
    tmp_ifc.write(util.fullpath(dist_ifc))
    dist_geom = dist_ifc.replace("ifc", "glb")
    print(os.path.normpath(util.fullpath(dist_geom)))
    subprocess.run(["ifcconvert", util.fullpath(dist_ifc), util.fullpath(dist_geom)])
    """
    Triangulation missing for face
      - 0zENsHqzbF0fWby$J$N5$n
      - 0zENsHqzbF0fWby$J$N5ne
      - 0zENsHqzbF0fWby$J$N5m$
      - 0zENsHqzbF0fWby$J$N5oE
    """


def removeBBox(ifc):
    for bbox in [rep for rep in ifc.by_type("IfcShapeRepresentation") if rep.RepresentationType == "BoundingBox"]:
        ifc.remove(bbox)
    return ifc
