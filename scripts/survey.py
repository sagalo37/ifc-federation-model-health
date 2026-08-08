import sys, glob, os, collections
import ifcopenshell
import ifcopenshell.util.element as elutil

for path in sorted(glob.glob(os.path.join(sys.argv[1], "*.ifc"))):
    f = ifcopenshell.open(path)
    prods = f.by_type("IfcProduct")
    els   = f.by_type("IfcElement")
    other = [p for p in prods if not p.is_a("IfcElement")]

    psets = qtos = typed = mats = 0
    for e in els:
        if elutil.get_psets(e, psets_only=True): psets += 1
        if elutil.get_psets(e, qtos_only=True):  qtos += 1
        if elutil.get_type(e):                   typed += 1
        if elutil.get_material(e):               mats += 1

    print("=" * 60)
    print(os.path.basename(path))
    print(f"  schema {f.schema_identifier}")
    print(f"  IfcProduct {len(prods)} / IfcElement {len(els)}")
    print(f"  typed {typed}  psets {psets}  qtos {qtos}  material {mats}")
    print("  elements:")
    for k, v in collections.Counter(e.is_a() for e in els).most_common():
        print(f"    {v:>4} {k}")
    print("  non-element products:")
    for k, v in collections.Counter(p.is_a() for p in other).most_common():
        print(f"    {v:>4} {k}")