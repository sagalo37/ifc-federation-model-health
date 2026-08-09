# Container register

Survey of the source containers as received, before any renaming or modification.
Counts produced with IfcOpenShell 0.8.5. `Typed`, `Psets`, `Qtos` and `Material`
count elements with at least one present, occurrence or inherited type.

| Container ID | Source file | Discipline | Schema | Spatial structure | Products | Elements | Typed | Psets | Qtos | Material | Element classes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PCERT-SMART-ZZ-ZZ-MO-ARC-0001 | Building-Architecture.ifc | Architecture | IFC4X3_ADD2 | Site (x2) > Building > Storey, + IfcSpatialZone | 22 | 15 | 12 | 1 | 7 | 14 | Wall (4), BuildingElementProxy (4), Slab (3), Chimney, EarthworksFill, Roof, Furniture |
| PCERT-SMART-ZZ-ZZ-MO-STR-0002 | Building-Structural.ifc | Structure | IFC4X3_ADD2 | Site (x2) > Building > Storey | 22 | 18 | 17 | 0 | 10 | 17 | Beam (6), Wall (4), BuildingElementProxy (3), DiscreteAccessory (2), Chimney, Footing, Roof |
| PCERT-SMART-ZZ-ZZ-MO-BSM-0003 | Building-Hvac.ifc | Mechanical | IFC4X3_ADD2 | Site (x2) > Building > Storey | 10 | 6 | 6 | 0 | 0 | 6 | BuildingElementProxy (2), AirTerminal (2), Chimney, DuctSegment |
| PCERT-SMART-ZZ-ZZ-MO-LND-0004 | Building-Landscaping.ifc | Landscape (building) | IFC4X3_ADD2 | Site (x2) | 9 | 7 | 6 | 0 | 0 | 7 | GeographicElement (4), BuildingElementProxy (3) |
| PCERT-SMART-ZZ-ZZ-MO-CBR-0005 | Infra-Bridge.ifc | Civil, bridge | IFC4X3_ADD2 | Site (x6) > Bridge (x3) > BridgePart (x18) | 77 | 50 | 46 | 0 | 15 | 48 | Beam (8), Member (8), Column (7), Footing (7), EarthworksFill (4), Wall (4), Sign (4), Slab (3), Railing (2), ElementAssembly (2), BuildingElementProxy |
| PCERT-SMART-ZZ-ZZ-MO-CRL-0006 | Infra-Rail.ifc | Civil, rail | IFC4X3_ADD2 | Site (x6) > Railway (x2) > RailwayPart (x2) | 85 | 75 | 75 | 0 | 0 | 73 | TrackElement (66), Rail (4), Course (2), ElementAssembly (2), BuildingElementProxy |
| PCERT-SMART-ZZ-ZZ-MO-CRD-0007 | Infra-Road.ifc | Civil, road | IFC4X3_ADD2 | Site (x6) > Road (x5) > RoadPart (x26) | 92 | 55 | 19 | 0 | 0 | 53 | SurfaceFeature (20), Course (16), EarthworksFill (16), ElementAssembly (2), BuildingElementProxy |
| PCERT-SMART-ZZ-ZZ-MO-BSH-0008 | Infra-Plumbing.ifc | Public health | IFC4X3_ADD2 | Site (x6) > Bridge (x3) | 38 | 29 | 29 | 0 | 0 | 25 | PipeSegment (24), ElementAssembly (4), BuildingElementProxy |
| PCERT-SMART-ZZ-ZZ-MO-LIN-0009 | Infra-Landscaping.ifc | Landscape (infra) | IFC4X3_ADD2 | Site (x8) > Road (x5) / Bridge (x3) / Railway (x2) | 130 | 112 | 107 | 0 | 0 | 102 | GeographicElement (76), Member (10), ElementAssembly (10), Sign (10), BuildingElementProxy (6) |
| **Total** | | | | | **485** | **367** | **317** | **1** | **32** | **345** | |

## Naming

Container IDs follow the UK National Annex 2021 seven-field structure:
Project-Originator-Functional-Spatial-Form-Discipline-Number.
Project and originator codes are invented for this exercise. Functional and spatial
breakdown are ZZ throughout: all containers cover the same scene with no functional
or spatial split. Discipline codes are three characters throughout, extending the
standard set so rail, road and bridge are distinguishable rather than collapsed into C.

## Notes

- All containers share the IfcProject name "ifc silly sample scene".
- Spatial structure differs by container: storey-based in the building files, facility/facility-part in the infra files. Both valid in 4.3.
- 1 element in 367 carries a property set.
- IfcBuildingElementProxy in all nine containers, 21 instances. LND-0004 is 3 of 7.
- Proxies split two ways: untyped placeholder geometry (Group#16-19, "underground - road", "underground - river") and deliberate coordination markers ("origin", "geo-reference", carrying the local coordination point and the map reference point). A blanket prohibition catches both.
- Qtos only in ARC, STR and CBR. 32 of 367.
- CRD-0007: 36 of 55 elements untyped. Every other container is at or near full type coverage.
- IfcEarthworksFill in the architectural container.
- Element naming inconsistent within a single storey in ARC.
- Rail count dominated by 66 repeated IfcTrackElement. Raw per-discipline counts are misleading.
- LIN-0009: 76 IfcGeographicElement, 21% of the whole federation.
- IfcElementAssembly present in six containers. Assemblies contain other elements, so counts overlap.
- IFCELEMENT does not work as an IDS applicability facet. Abstract supertypes match nothing, so classes have to be enumerated.
- IDS property facets take the measure type, not the quantity entity type. IFCLENGTHMEASURE, not IFCQUANTITYLENGTH.
- Containment requirement written against IfcBuildingStorey matches nothing in seven of nine containers.
- Clash test CBR against CRD, hard clash, 0 mm: 4 results, all overlapping geometry at the bridge/road interface. Modelling convention, not a coordination issue.