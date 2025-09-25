
(specs-layer-traffic-lights)=
# Infrastructure - Traffic Lights

Duckietown traffic lights are more than just blinking lights: they are static robots. Often referred to as "Duckiebots without wheels," they share many capabilities with the `DB18` Duckiebot models, minus the ability to move.

Traffic lights are urban robots equipped to:
- **Sense**: Detect the arrival of a Duckiebot using a camera.
- **Compute**: Perform onboard processing with a Raspberry Pi.
- **Communicate**: Signal other agents through LEDs and connect via Wi-Fi.

```{tip}
(For advanced Duckietowners only) Traffic lights are specialized cases of Duckietown Watchtowers, i.e., Watchtowers with LEDs. Watchtowers form the foundation of Duckietown Autolabs.
```

(specs-layer-traffic-lights-assembly)=
## Assembly

The assembly instructions for traffic lights are available here:

- [Traffic light assembly instructions](traffic-light-assembly-21)
- [Legacy traffic light assembly instructions](traffic-light-assembly-18)

(specs-layer-traffic-lights-placement)=
## Placement

Traffic lights are typically positioned diagonally over intersection tiles. Any intersection in Duckietown can host a traffic light.

```{note}
The lights must be installed at a height of 20 cm above the center of the intersection tile.
```

The computational stack is mounted in the appropriate housing and positioned outside the allowable driving region. The cables are integrated into the traffic light structure, as detailed in the [assembly instructions](specs-layer-traffic-lights-assembly).

Traffic light pillars must be positioned so that the embedded traffic signs adhere to the [appearance specifications](specs-layer-traffic-signs-placement).

```{figure} ../../_images/duckietown-city/appearance_specifications/traffic-lights/TrafficLight-DT18-TL.png
:name: subfig:traffic-light-dt18
:width: 90%

A Duckietown-compliant traffic light.
```

```{seo}
:description: Learn about Duckietown traffic lights as static robots with sensing, computing, and communication capabilities. Includes placement and assembly guidelines.
:keywords: Duckietown, traffic lights, robotics, Duckiebots, infrastructure, static robots, Raspberry Pi, urban robots, modular cities, assembly guide
```