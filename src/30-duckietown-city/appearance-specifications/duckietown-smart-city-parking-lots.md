
(specs-layer-parking-lots)=
# Layer - Parking Lots {bdg-warning} (`BETA`)

```{note}
The tile types described here are experimental. Use at your own risk!
```

Parking lots provide designated spaces for Duckiebots to "rest" when not in operation, adding realism and functionality to Duckietown cities. For an example application of parking lots in Duckietown, see this student ["Project Parking"](https://duckietown.com/autonomous-parking-in-duckietown/).

A parking lot introduces three additional tile types:

1. **Parking Lot Entry Tile**: Similar to a straight tile but with a red stop line in the middle. The parking lot sign ({numref}`subfig:parking`) must be visible from this stop line.
2. **Parking Spot Tiles**: Designated spaces for Duckiebots to park.
3. **Parking Spot Access Tiles**: Pathways connecting parking spots to the entry tile.

## Parking Lot Rules

To ensure a compliant parking lot design, follow these rules:

1. Each parking spot must occupy exactly one tile.
2. From any parking spot, there must be a clear, uninterrupted path to the parking lot entry tile, avoiding intersections with other parking spots. This ensures parked Duckiebots remain undisturbed.
3. From any position in a parking spot, a Duckiebot must have a clear view of at least two orthogonal lines or a sign with an AprilTag.

```{note}
If you are building parking lots in your Duckietown and would like to share your specifications, let us know!
``` 

```{seo}
:description: Learn about experimental parking lots in Duckietown, including tile types and rules for ensuring functional and compliant parking spaces for Duckiebots.
:keywords: Duckietown, parking lots, Duckiebots, parking tiles, robotics, experimental features, AprilTags, autonomous systems, robotics education
```
