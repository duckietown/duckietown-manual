(dtmatrix-dts-commands)=
# Duckiematrix - DTS Commands

```{seo}
:description: DTS (Duckietown Shell) commands for virtual Duckietown robots.
:keywords: Duckietown, Duckiematrix, virtual, robot, dts
```

This section describes `DTS` (`Duckietown Shell`) commands for virtual Duckietown robots.

```{needget}
- Successful Duckiematrix installation: [](duckiematrix-installation)
---
- Knowledge on `DTS` commands for virtual Duckietown robots
```

(intermediate-virtual-duckietown-robots-dts-commands-create)=
## Create

To create the virtual Duckietown robot `ROBOT_NAME`, run the following command, where `TYPE` and `CONFIGURATION` are its type and configuration, respectively:

```shell
dts duckiebot virtual create --type TYPE --configuration CONFIGURATION ROBOT_NAME
```

(intermediate-virtual-duckietown-robots-dts-commands-start)=
## Start

To start the virtual Duckietown robot `ROBOT_NAME`, run:

```shell
dts duckiebot virtual start ROBOT_NAME
```

(intermediate-virtual-duckietown-robots-dts-commands-connect)=
## Connect

To connect to the virtual Duckietown robot `ROBOT_NAME`, run:

```shell
dts duckiebot virtual connect ROBOT_NAME
```

(intermediate-virtual-duckietown-robots-dts-commands-list)=
## List

To list the existing virtual Duckietown robots and their statuses, run:

```shell
dts duckiebot virtual list
```

(intermediate-virtual-duckietown-robots-dts-commands-restart)=
## Restart

To restart the virtual Duckietown robot `ROBOT_NAME`, run:

```shell
dts duckiebot virtual restart ROBOT_NAME
```

(intermediate-virtual-duckietown-robots-dts-commands-stop)=
## Stop

To stop the virtual Duckietown robot `ROBOT_NAME`, run:

```shell
dts duckiebot virtual stop ROBOT_NAME
```

(intermediate-virtual-duckietown-robots-dts-commands-destory)=
## Destroy

To destroy the virtual Duckietown robot `ROBOT_NAME` and remove all of its Docker images, run:

```shell
dts duckiebot virtual destroy ROBOT_NAME
```
