# ===============
# Node Tree
# ===============


def create(tree, ifcobj, parentGUID, level, fn, fn1):
    objInfo = {"root": None, "parent": None, "children": []}
    is_ss_element = ifcobj.is_a("IfcSpatialStructureElement")
    if is_ss_element:
        op = ifcobj.ObjectPlacement
        if op:
            fn1(ifcobj, parentGUID)
        objInfo["root"] = ifcobj  # " - ".join([ifcobj.get_info().get(key) for key in ["GlobalId", "type"]])
        objInfo["parent"] = parentGUID
        tree[ifcobj.GlobalId] = objInfo
        fn(ifcobj)

    relaggrs = ifcobj.IsDecomposedBy
    for relaggr in relaggrs:
        ifcrelobjs = relaggr.RelatedObjects
        for relobj in ifcrelobjs:
            create(tree, relobj, ifcobj.GlobalId, level, fn, fn1)

    if is_ss_element:
        ces = ifcobj.ContainsElements
        for ce in ces:
            products = ce.RelatedElements
            for product in products:
                placement = product.ObjectPlacement
                if placement.is_a("IfcLocalPlacement"):
                    fn1(product, parentGUID)
                objInfo["children"].append(
                    product
                )  # " - ".join([product.get_info().get(key) for key in ["GlobalId", "type"]])
                fn(product)

    return tree
