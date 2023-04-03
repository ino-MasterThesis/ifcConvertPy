import sys

import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element

from core import gltf, ifc_info, node_tree, transmat

sys.path.append(".")

if __name__ == "__main__":
    ifc_file = ifcopenshell.open("../Assets/NTTcom.ifc")

    args = sys.argv
    assert len(args) > 1
    args = args[1]

    if args == "gLTF":

        def fn(element):
            gltf.create_geom(ifc_file.schema, element)

        def fn1(element, *args):
            pass

    elif args == "IFC_Info":

        def fn(element):
            ifc_info.create_info(element)

        def fn1(element, *args):
            pass

    elif args == "TransMat":

        def fn(element):
            pass

        def fn1(element, *args):
            transmat.save_transmat(element, *args)

    else:

        def fn(element):
            pass

        def fn1(element, *args):
            pass

    ifc_site = ifc_file.by_type("IfcSite")[0]
    print(f"-- Start {args} --")
    tree = node_tree.create({}, ifc_site, "", 0, fn, fn1)
    print(f"-- Done {args} --")
