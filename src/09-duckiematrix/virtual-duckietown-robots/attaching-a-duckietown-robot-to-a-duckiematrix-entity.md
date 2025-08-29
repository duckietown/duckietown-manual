(dtmatrix-attaching-virtual-robots)=
# Duckiematrix - Attaching Virtual Robots

```{seo}
:description: How to attach a Duckietown robot to a Duckiematrix entity.
:keywords: Duckietown, Duckiematrix, attach, robot, entity
```

This chapter describes how to attach a Duckietown robot to a Duckiematrix entity.

```{needget}
- Ability to run the Duckiematrix: [](dtmatrix-run)
---
- Knowledge on how to attach a Duckietown robot to a Duckiematrix entity
```

(introduction-attaching-a-duckietown-robot-to-a-duckiematrix-entity-introduction)=
## Introduction

For a Duckietown robot to act and sense inside the Duckiematrix, it needs a proxy inside the Duckiematrix (a Duckiematrix entity) to *attach* to.
A Duckietown robot outside the Duckiematrix is said to be *attached* to a Duckiematrix entity when all of its sensors and actuators are linked to their virtual counterparts inside the Duckiematrix.

To attach the Duckietown robot `ROBOT_NAME` to the Duckiematrix entity `ENTITY_NAME` (e.g., `map_0/vehicle_0`), run the following command, where `ENGINE_HOSTNAME` is the optional hostname (or IP address) of the `Engine`:

```shell
dts matrix attach [--engine ENGINE_HOSTNAME] ROBOT_NAME ENTITY_NAME
```

```{note}
This applies for both physical and virtual Duckietown robots.
```

```{tip}
Use the `--dreamwalk` option to enable dreamwalking for physical Duckiebots (i.e., commands will be sent to their physical actuators as well as their Duckiematrix counterparts).
```

```{attention}
Make sure that your computer's firewall is set to `inactive` or that an allow rule has been added for `ENGINE_HOSTNAME`.

To show the status of your computer's firewall, run:

    sudo ufw status

To add an allow rule for `ENGINE_HOSTNAME` to your computer's firewall, run:

    sudo ufw allow ENGINE_HOSTNAME
```
