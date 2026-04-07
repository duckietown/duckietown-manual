(dtmatrix-virtual-duckiebots)=
# Virtual Duckiebots

```{seo}
:description: Virtual Duckietown robots.
:keywords: Duckietown, Duckiematrix, virtual, robot
```
```{needget}
- Successful Duckiematrix installation: [](duckiematrix-how-to-start)
---
- Knowledge on virtual Duckietown robots.
```

(intermediate-virtual-duckietown-robots-introduction)=
## Introduction

Virtual Duckietown robots allow for a Duckietown robot's full software stack to be run on a local machine in its own
Docker environment, allowing for the full simulation of any aspect of that Duckietown robot, enabling integration tests.

Once a virtual Duckietown robot is running, it will behave in accordance with its physical equivalent,
including how it responds to `dts` commands.

The most common thing you will likely want to do is [create](intermediate-virtual-duckietown-robots-dts-commands-create)
a virtual robot and then [start](intermediate-virtual-duckietown-robots-dts-commands-start) it. Once it is up and running (you
see it when you run the command `dts fleet discover` just like any other Duckiebot), you probably will want to
[attach](introduction-attaching-a-duckietown-robot-to-a-duckiematrix-entity-introduction) it to an entity in the Duckiematrix. Once this attachment is complete,
all the data that is collected by the entity in the Duckiematrix will be fed to the virtual robot and, conversely, any
control actions that you take with your virtual Duckiebot will be executed on the entity in the Duckiematrix. See
[below](intermediate-virtual-duckietown-robots-drivers-introduction) for
a detailed description of the supported drivers that you can use to send or receive data.

## The Virtual Robot `dts` API

Like most things in Duckietown, the primary way to perform operations on virtual robots is through the Duckietown Shell (`dts`)

The following is a list of operations you can perform:

(intermediate-virtual-duckietown-robots-dts-commands-create)=
### Create

To create the virtual Duckietown robot `ROBOT_NAME`, run the following command, where `TYPE` and `CONFIGURATION` are its type and configuration, respectively:

```shell
dts duckiebot virtual create --type TYPE --configuration CONFIGURATION ROBOT_NAME
```

for example, 

```shell
dts duckiebot virtual create --type duckiebot --configuration DB21J myduckiebot
```

(intermediate-virtual-duckietown-robots-dts-commands-start)=
### Start

To start the virtual Duckietown robot `ROBOT_NAME`, run:

```shell
dts duckiebot virtual start ROBOT_NAME
```

(intermediate-virtual-duckietown-robots-dts-commands-connect)=
### Connect

To connect to the virtual Duckietown robot `ROBOT_NAME`, run:

```shell
dts duckiebot virtual connect ROBOT_NAME
```

(intermediate-virtual-duckietown-robots-dts-commands-list)=
### List

To list the existing virtual Duckietown robots and their statuses, run:

```shell
dts duckiebot virtual list
```

(intermediate-virtual-duckietown-robots-dts-commands-restart)=
### Restart

To restart the virtual Duckietown robot `ROBOT_NAME`, run:

```shell
dts duckiebot virtual restart ROBOT_NAME
```

(intermediate-virtual-duckietown-robots-dts-commands-stop)=
### Stop

To stop the virtual Duckietown robot `ROBOT_NAME`, run:

```shell
dts duckiebot virtual stop ROBOT_NAME
```

(intermediate-virtual-duckietown-robots-dts-commands-destory)=
### Destroy

To destroy the virtual Duckietown robot `ROBOT_NAME` and remove all of its Docker images, run:

```shell
dts duckiebot virtual destroy ROBOT_NAME
```


(introduction-attaching-a-duckietown-robot-to-a-duckiematrix-entity-introduction)=
## Attaching Virtual Robots

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

(intermediate-virtual-duckietown-robots-drivers-introduction)=
## Supported Drivers

Virtual Duckietown robot drivers allow for the communication between a Duckietown robot's ROS stack and an entity inside the Duckiematrix.

```{figure} ../../_images/duckiematrix/intermediate/virtual_duckietown_robots/virtual-duckietown-robot-drivers.png
:name: fig:virtual-duckietown-robot-drivers
:alt: Data types exchanged with the Duckiematrix by the virtual Duckietown robot drivers.

Data types exchanged with the Duckiematrix by the virtual Duckietown robot drivers.
```

(intermediate-virtual-duckietown-robots-duckiedrone-mavlink)=
### Duckiedrone MAVLink Proxy Integration

The virtual Duckiedrone uses a hybrid integration architecture. Like ground-based virtual Duckiebots, it uses direct driver bindings for sensors such as the camera and Time-of-Flight (ToF). However, for flight control and IMU data, it relies on a MAVLink proxy routed through DTPS (Duckietown Postal Service).

The following diagram illustrates how the components are connected:

```{figure} ../../_images/duckiematrix/diagrams/mavlink_proxy_connections.drawio.png
:name: fig:mavlink-proxy-connections
:alt: Architecture of the MAVLink proxy connections between the Duckiematrix and a virtual Duckiedrone.

Architecture of the MAVLink proxy connections between the Duckiematrix and a virtual Duckiedrone.
```

The key components of this integration are:

* **RotorPy** — a physics simulator for multirotor vehicles running inside the Duckiematrix Engine. It simulates the drone's flight dynamics and produces sensor readings.
* **PX4 SITL** — the PX4 flight controller running in Software-In-The-Loop mode on the virtual robot's Docker environment.
* **MAVLink** — the communication protocol used between PX4 SITL and the rest of the system (e.g., MAVROS2 ROS nodes).
* **DTPS MAVLink Proxy** — a proxy that routes MAVLink messages over DTPS topics, bridging the PX4 SITL running on the virtual robot with the RotorPy simulation running inside the Duckiematrix Engine.

(intermediate-virtual-duckietown-robots-drivers-implementation-status)=
### Implementation status

```{list-table}
:header-rows: 1
:name: table:virtual-duckietown-robots-drivers

* - Driver
  - Implemented
* - Camera
  - Yes
* - Time-of-Flight
  - Yes
* - IMU
  - Yes
* - LED
  - Yes
* - Encoder
  - Yes
* - Wheel
  - Yes
```
