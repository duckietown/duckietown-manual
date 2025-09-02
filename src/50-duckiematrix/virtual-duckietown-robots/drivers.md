(dtmatrix-drivers)=
# Duckiematrix - Drivers

```{seo}
:description: Virtual Duckietown robot drivers.
:keywords: Duckietown, Duckiematrix, virtual, robot, drivers
```

This section describes virtual Duckietown robot drivers.

```{needget}
- Successful Duckiematrix installation: [](duckiematrix-installation)
---
Knowledge on virtual Duckietown robot drivers.
```

(intermediate-virtual-duckietown-robots-drivers-introduction)=
## Introduction

Virtual Duckietown robot drivers allow for the communication between a Duckietown robot's ROS stack and an entity inside the Duckiematrix.

```{figure} ../../_images/duckiematrix/intermediate/virtual_duckietown_robots/virtual-duckietown-robot-drivers.png
:name: fig:virtual-duckietown-robot-drivers
:alt: Data types exchanged with the Duckiematrix by the virtual Duckietown robot drivers.

Data types exchanged with the Duckiematrix by the virtual Duckietown robot drivers.
```

(intermediate-virtual-duckietown-robots-drivers-implementation-status)=
## Implementation status

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
