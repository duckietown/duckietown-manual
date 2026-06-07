(ops-db-subsys-make-it-shine)=
# LED control (Make it Shine!)

```{seo}
:description: Learn how to actuate the Duckiebot addressable light emitting diodes (LEDs) changing color and intensity.
:keywords: Duckietown, Duckiebot, LEDs, change LED color, change LED intensity, LED Controller
```

```{needget}
- A correctly assembled Duckiebot: [](db-testing-hw-components)
- (for most methods) A functional `dts` installation: [](setup-dts)
- You can ping the Duckiebot with `ping ROBOTNAME.local`. If not: [](setup-duckiebot-network)
---
- Control the Duckiebot's LEDs intensity and color
```

Duckiebots have four LEDs, positioned similarly to the head and tail lights on a car. This section describes how to control the LEDs on your Duckiebot through the `LED Controller`.

```{figure} ../../_images/software_tools/led_controller/leds_layout.png
A Duckiebot with the LEDs shining white (left) and a diagram with arrows indicating the front and back LEDs (right).
```

## Using LEDs on Duckiebots

LEDs are more than just lights. As proper actuators on a Duckiebot, they can be used for many purposes, including but not limited to:

* Indicating what mode or mission the Duckiebot is running
* Communicating state changes in the controller
* Signaling upcoming turns or other navigational plans
* Expressing character and personality
* Lighting the driving environment.

A manual way to control your Duckiebot's LEDs is by using the `LED Controller`.

```{figure} ../../_images/software_tools/led_controller/led_controller.png
:name: led_controller
:alt: The Duckietown GUI for LED control
:width: 60%
:align: center

The `LED Controller` interface is a simple way for controlling color and intensity of the Duckiebot's LEDs.
```
:::::{tab-set}
::::{tab-item} Ubuntu

To open the `LED Controller`, first make sure you can successfully ping the Duckiebot with `ping ROBOT_NAME.local`, then run:

```shell
dts duckiebot led_control ROBOT_NAME
```

where `ROBOT_NAME` is the hostname of either a physical or virtual Duckiebot.  

::::

::::{tab-item} Duckietown Workspace

There are two ways to open the `LED Controller`: 

1. If you have installed `dts` on the host machine: open a terminal on your host machine and run:

    dts duckiebot led_control ROBOT_NAME

```{note}
The first time a robot app is ran, a popup window may appear asking for permissions. Insert your password and "(Always) Allow" to continue. 
```

2. Alternatively, inside the Workspace terminal run:

    dts duckiebot led_control ROBOT_NAME --browser

where `ROBOT_NAME` is the hostname of either a physical or virtual Duckiebot.  

::::
:::::

<!--
```{note}
{{ dt_workspace_duckietown_viewer_note.format(dt_workspace_note_prefix, "led_control") }}
```
-->

To control your Duckiebot's LEDs, use the buttons and sliders to change their colors and intensities, respectively.

Note the keys in the table below.

```{list-table}
:header-rows: 1
:name: table:led-controller-commands

* - Key
  - Function
* - <kbd>R</kbd>
  - Refresh the window
* - <kbd>T</kbd>
  - Open the `Debug Console`
```

```{note}
The color dropper tool is not operational yet.
```

## Troubleshooting

```{trouble}
I can see messages being sent to my Duckiebot when looking at the `DUCKIEBOT_NAME/actuator/lights/base/pattern` `DTPS` topic, after following [](sw-tools-dtps), but the LEDs do not update and the `Components` page of the `Dashboard` (opened by running `dts duckiebot dashboard DUCKIEBOT_NAME --page robot/components`) shows a red alert for the HUT.
---
If you have a HUT v3.1, follow [](reflash-microcontroller).
```

```{trouble}
My Duckiebot's LEDs do not update and I cannot see messages being sent to my Duckiebot when looking at the `DUCKIEBOT_NAME/actuator/lights/base/pattern` `DTPS` topic, after following [](sw-tools-dtps).
---
Reach out for help: [](how-to-get-help)
```

```{trouble}
I have re-flashed the HUT but the LEDs still do not update. Additionally, the ToF sensor and front bumper are not detected on the `Components` page of the `Dashboard` (opened by running `dts duckiebot dashboard DUCKIEBOT_NAME --page robot/components`). I may also be having issues with the screen.
---
Disconnect the ToF sensor from the front bumper and use the long I2C cable, that originally connected the front bumper to the HUT, to connect the ToF sensor directly to that same HUT port. Finally, reboot your Duckiebot. This procedure bypasses a known multiplexer issue on some front bumpers that can cause other issues with the HUT.
```

```{trouble}
I have connected the ToF sensor directly to the same HUT port that the front bumper was originally connected to and rebooted my Duckiebot but the LEDs still do not update.
---
Make sure that the `duckiebot-interface` container is running by checking the `Portainer` page of the `Dashboard` (opened by running `dts duckiebot dashboard DUCKIEBOT_NAME --page portainer`) or by running:

    `docker -H DUCKIEBOT_NAME.local ps`

The exact name of the container will depend on your Duckiebot's version. If you do not see the `duckiebot-interface` container, update your Duckiebot by running:

    `dts duckiebot update DUCKIEBOT_NAME`
```