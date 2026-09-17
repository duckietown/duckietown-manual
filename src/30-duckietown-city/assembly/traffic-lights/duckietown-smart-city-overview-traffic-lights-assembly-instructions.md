```{seo}
:description: Learn how to assemble and set up traffic lights in Duckietown, from hardware installation to SD-card preparation and behavior launching.
:keywords: Duckietown, traffic lights, robotics, Duckiebots, assembly guide, SD-card preparation, Autolab, watchtower network, intersection control
```

(traffic-light-assembly)=
# Assembly - Traffic Light

```{needget}
- Traffic light components ([Duckietown project shop](https://get.duckietown.com/products/smart-traffic-light))

- An appropriately [configured SD-card](setup-db-sd-card-flashing-intro).

- Tools: (strong) wood glue or hot glue gun, tape, double-sided tape.
---
- An assembled traffic light in configuration `DT21-TL` (latest) or previous legacy versions.
```

This section describes the physical assembly and installation of traffic lights.

## Overview

Traffic lights are crucial elements of modern cities, and in Duckietown, they play a similar role by ensuring well-organized traffic.

They can serve as:

1. Centralized coordinators of traffic at 3- or 4-way intersections in Duckietown.

2. Components of a Duckietown Autolab watchtower network.

```{attention}
For Duckiebots to recognize traffic lights governing a specific intersection, appropriate signage must be placed (traffic light traffic sign instead of a stop sign).
```

- __Hardware Design__: Traffic lights are "Duckiebots without wheels," housed in a distinct chassis.

- __Structure__: They consist of two supports connected by an overhanging tube, with one support containing the computational stack and an overseeing camera.

- __Placement__: Traffic lights are positioned diagonally at intersections.

## Hardware Assembly

- For __latest__ configuration traffic lights, refer to the instructions:

  - [](traffic-light-assembly-21)

- For legacy builds (prior to `TL21`), follow these instructions:

  - [](traffic-light-assembly-18).

(dt-ops-tl-prep)=
### SD card image Preparation

At the software level, traffic lights function similarly to Duckiebots. When initializing the SD-card, follow the [Duckiebot SD-card initialization instructions](setup-db-sd-card-flashing-intro), ensuring that you use the `--type traffic_light` option.

Wi-Fi configuration for traffic lights is not set by default. To enable it, use the `--wifi` option as described in the [instructions](setup-db-sd-card-flashing-intro).

Example command for a Wi-Fi connected traffic light:

```shell
dts init_sd_card --hostname ROBOTNAME --country COUNTRY --type traffic_light --configuration TL21
```

```{note}
For Autolab users: Use the convention `hostname: watchtowerXX`, where `XX` are incremental numbers.
```

- For standard traffic light setup, use:

  - `hostname: trafficlightXX`

- Login account:

  - Username: `duckie`

  - Password: the value entered when DTS prompts during initialization

```{warning}
For Autolab users, retain the `duckie` username and record the password for each device.
```

(tl-first-boot)=
### Traffic Light First Boot

Once the traffic light is fully assembled, turn it on and follow the [first boot](duckiebot-boot) procedure, and once finished update the software with:

    dts duckiebot update ROBOTNAME

If prompted, select `robot type = duckiebot` and `robot hardware = raspberry_pi`. Wait for the update to finish and reboot the device.

The blinking behavior should then start automatically.

<!--
Semantics of LEDS {#LED-semantics status=draft}

headlights: white, constant

Assumption:

- __20 fps__ to do LED detection

- 1s to decide

- 3 frequencies to detect

tail lights: red, __6 hz square wave__

traffic light "GO" = green, __1 hz square wave__

traffic light "STOP" = red, __1.5 Hz__ square wave**

duckie light on top, state 0 = off

duckie light on top, state 1 = blue, __3 Hz, square wave__

duckie light on top, state 2 = ?, __2.5 Hz square wave__

duckie light on top, state 3 = ?, __2 Hz square wave__

verify if this info is still up to date.
-->
