| File | Schema | Spatial structure | Products | Elements | Typed | Psets | Qtos | Material | Element classes |
|---|---|---|---|---|---|---|---|---|---|
| Building-Architecture.ifc | IFC4X3_ADD2 | Site (x2) > Building > Storey, + IfcSpatialZone | 22 | 15 | 12 | 1 | 7 | 14 | Wall (4), BuildingElementProxy (4), Slab (3), Chimney, EarthworksFill, Roof, Furniture |
| Building-Hvac.ifc | IFC4X3_ADD2 | Site (x2) > Building > Storey | 10 | 6 | 6 | 0 | 0 | 6 | BuildingElementProxy (2), AirTerminal (2), Chimney, DuctSegment |
| Building-Landscaping.ifc | IFC4X3_ADD2 | Site (x2) | 9 | 7 | 6 | 0 | 0 | 7 | GeographicElement (4), BuildingElementProxy (3) |
| Building-Structural.ifc | IFC4X3_ADD2 | Site (x2) > Building > Storey | 22 | 18 | 17 | 0 | 10 | 17 | Beam (6), Wall (4), BuildingElementProxy (3), DiscreteAccessory (2), Chimney, Footing, Roof |
| Infra-Bridge.ifc | IFC4X3_ADD2 | Site (x6) > Bridge (x3) > BridgePart (x18) | 77 | 50 | 46 | 0 | 15 | 48 | Beam (8), Member (8), Column (7), Footing (7), EarthworksFill (4), Wall (4), Sign (4), Slab (3), Railing (2), ElementAssembly (2), BuildingElementProxy |
| Infra-Landscaping.ifc | IFC4X3_ADD2 | Site (x8) > Road (x5) / Bridge (x3) / Railway (x2) | 130 | 112 | 107 | 0 | 0 | 102 | GeographicElement (76), Member (10), ElementAssembly (10), Sign (10), BuildingElementProxy (6) |
| Infra-Plumbing.ifc | IFC4X3_ADD2 | Site (x6) > Bridge (x3) | 38 | 29 | 29 | 0 | 0 | 25 | PipeSegment (24), ElementAssembly (4), BuildingElementProxy |
| Infra-Rail.ifc | IFC4X3_ADD2 | Site (x6) > Railway (x2) > RailwayPart (x2) | 85 | 75 | 75 | 0 | 0 | 73 | TrackElement (66), Rail (4), Course (2), ElementAssembly (2), BuildingElementProxy |
| Infra-Road.ifc | IFC4X3_ADD2 | Site (x6) > Road (x5) > RoadPart (x26) | 92 | 55 | 19 | 0 | 0 | 53 | SurfaceFeature (20), Course (16), EarthworksFill (16), ElementAssembly (2), BuildingElementProxy |
| **Total** | | | **485** | **367** | **317** | **1** | **32** | **345** | |


## Notes

- Same IfcProject name across all containers, so they federate.
- Spatial structure differs: storey-based in building files, facility/facility-part in infra. Both valid in 4.3.
- IfcEarthworksFill in Building-Architecture. Wrong container.
- 2x IfcBuildingElementProxy, "Group#18" and "Group#19", in Building-Architecture.
- Naming inconsistent within one storey.
- Rail count dominated by 30 repeated sleepers. Skews per-discipline counts.
- No Psets anywhere so far, occurrence or type. Qtos on IfcWall, none on IfcRail.