```{seo}
:description: Learn how to move a Duckiebot differential drive robot through the Duckietown keyboard controller.
:keywords: Duckiebot, Keyboard Controller, how to move a duckiebot, duckiebot remote control, duckiebot open loop control, make it move, dc motor control via keyboard
```

```{needget}
- A correctly assembled, powered on, Duckiebot: [](db-testing-hw-components)
- (for most methods) A functional `dts` installation: [](setup-dts)
- You can ping the Duckiebot with `ping ROBOTNAME.local`. If not: [](setup-duckiebot-network)
---
- Keyboard control of a Duckiebot
```

(ops-db-subsys-make-it-move)=
# Keyboard Control (Make it Move!)

An easy way to make your Duckiebot move is by using the `Keyboard Controller`.

```{figure} ../../_images/software_tools/keyboard_controller/keyboard_controller.png
:name: keyboard_controller
:align: center
:width: 70%
:alt: the Duckietown keyboard controller is a tool that enables manual keyboard control of Duckiebots

The Keyboard Controller enables manual control of the Duckiebot.
```

:::::{tab-set}

::::{tab-item} Ubuntu

To open the `Keyboard Controller`, first make sure you can successfully ping the Duckiebot with `ping ROBOT_NAME.local`, then run:

```shell
dts duckiebot keyboard_control ROBOT_NAME
```

where `ROBOT_NAME` is the hostname of either a physical or virtual Duckiebot.  

::::

::::{tab-item} Duckietown Workspace

There are two ways to open the Keyboard Controller: 

1. If you have installed `dts` on the host machine: open a terminal on your host machine and run:

    dts duckiebot keyboard_control ROBOT_NAME

```{note}
The first time this command is ran, a popup window will appear asking for permissions. Insert your password and "(Always) Allow" to continue. 
```

2. Alternatively, inside the Workspace terminal run:

    dts duckiebot keyboard_control ROBOT_NAME --browser

where `ROBOT_NAME` is the hostname of either a physical or virtual Duckiebot.  

::::
:::::

<!--
```{note}
{{ dt_workspace_duckietown_viewer_note.format(dt_workspace_note_prefix, "keyboard_control") }}
```
-->
Note the keys in the table below.

```{list-table}
:header-rows: 1
:name: table:keyboard-controller-commands

* - Key
  - Function
* - <kbd>W</kbd>
  - Drive forwards
* - <kbd>S</kbd>
  - Drive backwards
* - <kbd>A</kbd>
  - Turn left
* - <kbd>D</kbd>
  - Turn right
* - <kbd>E</kbd>
  - Toggle the `Emergency Stop` switch
* - <kbd>F</kbd>
  - Toggle the `Autopilot` switch
* - <kbd>X</kbd>
  - Increase the `Gain`
* - <kbd>Z</kbd>
  - Decrease the `Gain`
* - <kbd>V</kbd>
  - Increase the `Trim`
* - <kbd>C</kbd>
  - Decrease the `Trim`
* - <kbd>Space</kbd>
  - Save the `Gain` and `Trim`
* - <kbd>R</kbd>
  - Refresh the window
* - <kbd>T</kbd>
  - Open the `Debug Console`
```

```{note}
The <kbd>F</kbd> key's function (`Autopilot`) requires software, such as for [](duckiebot-demo-lf), to be running.
```

(keyboard-controller-troubleshooting)=
## Troubleshooting

```{trouble}
My Duckiebot does not move.
---
Before trying to use the `Keyboard Controller`, make sure that it is active by selecting its window.
```

```{trouble}
The `Keyboard Controller` window is active but my Duckiebot still does not move. However, I can see messages being sent to my Duckiebot when looking at the `DUCKIEBOT_NAME/actuator/wheels/base/pwm` `DTPS` topic, after following [](sw-tools-dtps), and the `Components` page of the `Dashboard` (opened by running `dts duckiebot dashboard DUCKIEBOT_NAME --page robot/components`) shows a red alert for the HUT.
---
If you have a HUT v3.1, follow [](reflash-microcontroller).
```

```{trouble}
I have re-flashed the HUT but my Duckiebot still does not move or moves in a jerky manner. Additionally, the ToF sensor and front bumper are not detected on the `Components` page of the `Dashboard` (opened by running `dts duckiebot dashboard DUCKIEBOT_NAME --page robot/components`). I may also be having issues with the screen.
---
Disconnect the ToF sensor from the front bumper and use the long I2C cable, that originally connected the front bumper to the HUT, to connect the ToF sensor directly to that same HUT port. Finally, reboot your Duckiebot. This procedure bypasses a known multiplexer issue on some front bumpers that can cause other issues with the HUT.
```

```{trouble}
I have  connected the ToF sensor directly to the same HUT port that the front bumper was originally connected to and rebooted my Duckiebot but it still does not move.
---
Make sure that the `duckiebot-interface` container is running by checking the `Portainer` page of the `Dashboard` (opened by running `dts duckiebot dashboard DUCKIEBOT_NAME --page portainer`) or by running:

    `docker -H DUCKIEBOT_NAME.local ps`

The exact name of the container will depend on your Duckiebot's version. If you do not see the `duckiebot-interface` container, update your Duckiebot by running:

    `dts duckiebot update DUCKIEBOT_NAME`
```

```{trouble}
My Duckiebot drives backwards when I command it to drive forward.
---
Swap the motor cable connections on the HUT.
```

```{trouble}
My Duckiebot doesn't go really straight when I command it to. At least not for long.
---
Perform the wheel calibration procedure: [](db-wheels-calibration).
```