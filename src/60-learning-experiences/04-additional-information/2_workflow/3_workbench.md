```{seo}
:description: Learn how to use the `dts code workbench` command to run Duckietown Learning Experience code on a simulated or real Duckiebot, with various flags for different configurations.
:keywords: Duckietown, dts code workbench, ROS container, simulated Duckiebot, real Duckiebot, learning experience, agent code
```

(behind-the-scenes-code-workbench)=
# `dts code workbench`
 
 This command allows us to run the learning experience code on either a simulated or a real Duckiebot.
 
 ## No flags
 
 When no flags are given, only a ROS container is run and the VNC allows us to have a virtual desktop to connect to it.

 ```{figure} ../../_images/lx-devmanual/background/workbench-no-flag.drawio.png
:name: workbench-no-flag-1
:alt: Containers running on the Duckiebot and base station with the --local flag
:align: center
:width: 90%
 
 Containers running on the Duckiebot and base station with the `--local` flag
 ```
 
 ## `--sim` flag
 
 <!-- [`ex-modcon-experiment-manager`, `ex-modcon-simulator`, `ex-modcon-ros`, `ex-modcon-vnc`, `ex-modcon-agent`] -->
 With the `--sim` flag, the code is executed on the local machine and communicates with a simulator of the Duckiebot.
 
 ```{figure} ../../_images/lx-devmanual/background/workbench-sim-scheme.drawio.png
:name: workbench-sim-1
:alt: Containers running on the Duckiebot and base station
:align: center
:width: 90%

 Containers running on the Duckiebot and base station
 ```
 
 ## `--duckiebot` flag
 
 With the `--duckiebot` flag we execute the agent code on the real Duckiebot.
 The communication between the FIFO bridge and the ROS stack of the real Duckiebot enables the agent to control the Duckiebot.
 
 ```{figure} ../../_images/lx-devmanual/background/workbench-duckiebot-scheme.png
:name: workbench-duckiebot-1
:alt: Containers running on the Duckiebot and base station
:align: center
:width: 90%
 
 
 Containers running on the Duckiebot and base station
 ```
 
 ## `--local` flag
 
 When the `--local` flag is passed, the agent, the FIFO bridge and the other ROS container are executed on the local machine.
 The communication between the FIFO bridge and the ROS stack of the real Duckiebot enables the agent to control the Duckiebot.
 
 ```{figure} ../../_images/lx-devmanual/background/workbench-duckiebot-scheme-local.drawio.png
:name: workbench-duckiebot-local-1
:alt: Containers running on the Duckiebot and base station with the `--local` flag
:align: center
:width: 90%
 
 Containers running on the Duckiebot and base station with the `--local` flag
 ```