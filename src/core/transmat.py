import json

import numpy as np
from scipy.spatial.transform import Rotation

from util import util
from util.matrix4 import Matrix4

# ==============================
# Transform Matrix
# ==============================


def save_transmat(element, parentGUID):
    placement = element.ObjectPlacement
    trans = create_transmat(placement, parentGUID)
    dist_json = util.fullpath(f"../../dist/trans/{element.GlobalId}.json")
    with open(dist_json, mode="w") as f:
        json.dump({"transform": trans.tolist()}, f, indent=4, ensure_ascii=False)
        print(f"save to {dist_json}")


def create_transmat(placement, parentGUID):
    trans = Matrix4()

    axis2placement = placement.RelativePlacement
    if not not axis2placement:
        factor = 0.001  # おそらく単位は [mm]
        loc = Matrix4().makeTranslation(*[k * factor for k in axis2placement.Location.Coordinates])
        quat = Matrix4().makeRotationFromQuaternion([0.0, 0.0, 0.0, 1.0])

        trans = quat.premultiply(loc)

        axis = axis2placement.Axis
        refDir = axis2placement.RefDirection
        if not (not axis or not refDir):
            axis = create_numpy_vector_cs(axis[0])
            refDir = create_numpy_vector_cs(refDir[0])
            rot = np.cross(refDir, axis)
            quat = Matrix4().makeRotationFromQuaternion(Rotation.from_rotvec(rot).as_quat().tolist())

    placement_rel_to = placement.PlacementRelTo
    if not not placement_rel_to:
        objs = placement_rel_to.PlacesObject
        is_found = False
        for obj in objs:
            is_found = obj.GlobalId == parentGUID
            if is_found:
                break
        if not is_found:
            trans.multiply(create_transmat(placement_rel_to, parentGUID))

    return trans


def create_numpy_vector_cs(v, rightHanded=True):
    if rightHanded:
        return np.array([v[0], -v[1], v[2]])
    else:
        return np.array(v)
