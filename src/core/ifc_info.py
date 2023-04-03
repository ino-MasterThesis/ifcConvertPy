import json

import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element

from util import util

# ===============
# Info Tree
# ===============


def create_info(element):
    def convertEntity2Str(d):
        for k, v in d.items():
            if v.__class__ == ifcopenshell.entity_instance:
                d[k] = "#".join([str(v.get_info().get(target_key)) or "***" for target_key in ["type", "id"]])
        return d

    try:
        base_info = element.get_info()
        psets = ifcopenshell.util.element.get_psets(element)
        util_type = ifcopenshell.util.element.get_type(element)
        if util_type is not None:
            psets2 = ifcopenshell.util.element.get_psets(util_type)
        else:
            psets2 = {}
        j = deep_merge_dict(deep_merge_dict(psets, psets2), base_info)
    except Exception as e:
        raise e

    dist_json = util.fullpath(f"../../dist/ifcinfo/{element.GlobalId}.json")
    with open(dist_json, mode="w") as f:
        j = convertEntity2Str(j)
        json.dump(j, f, indent=4, ensure_ascii=False)
        print(f"save to {dist_json}")


def deep_merge_dict(d1, d2):
    acc = d1.copy()
    for k, v in d2.items():
        if isinstance(v, dict) and isinstance(acc[k], dict):
            acc[k] = deep_merge_dict(acc[k], v)
        else:
            acc[k] = v
    return acc
