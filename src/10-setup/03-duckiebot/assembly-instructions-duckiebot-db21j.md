```{seo}
:description: Assembly procedure for a Duckiebot DB21J.
:keywords: Duckietown, Duckiebot, DB21J, assembly instructions, how to build a Duckiebot, how to assemble a Duckiebot
```

(assembly-instructions-db21j)=
# Assembly Instructions (`DB21J`)

This section describes the assembly procedure for your Duckiebot DB21J.

```{needget}
- The components for a Duckiebot `DB21-J4` (available on the [Duckietown online store](https://get.duckietown.com)).
---
An assembled Duckiebot DB21J.
```

```{seealso}
The most recent Duckiebot variant is slightly different from what shown below. It includes:
- a plastic omnidirectional, instead of a metal one

- a set of M3 nylon screws and nuts, instead of the same in metal.

Follow the instructions in this page, but:

- replace steps 4 and 5 with these instruction: [](assembly-instructions-db21j-v3)

- use nylon screws and nuts instead of metal ones when placing them in the chassis.  
```

```{admonition} What is in the box and assembly video (DB21M)
<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/528621827?h=44014b1b93" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
<p><a href="https://vimeo.com/528621827">Duckiebot DB21M unpacking and assembly</a> from <a href="https://vimeo.com/duckietown">Duckietown</a> on <a href="https://vimeo.com">Vimeo</a>. Note this video is not from a DB21J4, and details differ.</p>
```

(db21j-preliminary-steps)=
## Preliminary steps

### Unboxing

Unbox all of the components within your Duckiebox and lay them out on a flat surface.
Ensure that you have well-lit, uncluttered space to work on.
Although not necessary, a small (`M2.5`) wrench and pliers may ease some passages.

```{figure} ../../_images/assembly/db21j/db21-allcomponents.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-allcomponents
:alt: Components included in the DB21J Duckiebot kit.

The contents of a DB21J Duckiebox.
```

```{note}
Your Duckiebot chassis may be under the white protective foam inside the Duckiebox.
To reach it, pull the white foam out of the box after removing everything else.
Note that the upper part of the inside foam has several side pockets in addition to a main compartment where components are located.
```

### Plastic cover

Peel off the plastic covers from both sides of every chassis component.

### Connecting components

Verify each connecting component (screws, nuts and stand-offs) before using them as this may prevent undesirable effects (e.g., nylon screws prevent electrical shorts, bigger screws may damage the chassis, etc.).
There are also shorter screws, which can be used in some cases.

```{figure} ../../_images/assembly/db21j/db21-rev1-parts-indices.png
:alt: Indexed components used to assemble a DB21J Duckiebot.
:name: fig:db21m-rev1-parts-indices

Connecting components.
```

### HUT

The HUT an electronics board containing the connectors for various sensors (e.g., fan, motors, top button, etc.) that is mounted to the Jetson Nano.

```{figure} ../../_images/assembly/db21j/db21-rev1-hut_00.png
:alt: DB21J hardware utility tool (HUT) board.
:name: fig:db21-rev1-hut_00

The HUT.
```

```{figure} ../../_images/assembly/db21j/db21-rev1-1-hut_01.png
:alt: DB21J hardware utility tool (HUT) board with its connectors identified.
:name: fig:db21-rev1-hut_01

The HUT's components.
```

(charge-duckiebattery-via-the-hut)=
### Charging the Duckiebattery via the HUT

This preliminary step allows the Duckiebattery to begin charging while confirming the functionality of the HUT.

To charge the Duckiebattery via the HUT:

- Connect the Duckiebattery to the HUT as shown below and make sure that a green LED on the HUT is lit.

- Wait `30 min` and then press the button on the Duckiebattery.

- Check that the state of charge LEDs on the Duckiebattery start blinking.

- Leave this setup until the Duckiebattery is charged (this may take up to `5 h`).

```{figure} ../../_images/assembly/db21j/db21-rev1-step_00.png
:alt: DB21J Duckiebattery connected to the hardware utility tool for charging.
:name: fig:db21-rev1-step_00

The Duckiebattery charging via the HUT.
```

```{note}
For more information on the Duckiebattery, follow [](db-opmanual-dtbattery-v2).
```

(howto-camera-assembly-db21)=
## Camera assembly

This section describes the steps to assemble the *camera assembly*.

### Step 1

Substeps:

1. Gently open but do not remove the camera cable connector on the camera PCB as shown below.

2. Connect the camera cable to the camera cable connector on the camera PCB such that the pins on the camera cable come into contact with those in the camera cable connector on the camera PCB as shown below (the blue strip on the camera cable should face away from the camera PCB).

3. Close the camera cable connector on the camera PCB as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_01.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-01
:alt: DB21J Duckiebot assembly, step 1.
```

### Step 2

Substeps:

1. From the front side of the camera holder, feed the camera cable through the slot in the camera holder as shown below.

2. Screw the camera PCB onto the front side of the camera holder using four `N2x8` screws and four `N2` nuts as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_02.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-02
:alt: DB21J Duckiebot assembly, step 2.
```

(db21j-bottom-assembly)=
## Bottom assembly

This section describes the steps to assemble the *bottom assembly*.

```{figure} ../../_images/assembly/db21j/db21-rev1-overview-step_03-18.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-overview-step-03-18
:alt: Overview of DB21J Duckiebot bottom assembly steps 3 through 18.

DB21J Duckiebot bottom assembly overview.
```

```{note}
From [](db21j-bottom-assembly-step-3) to [](db21j-bottom-assembly-step-15), the bottom side of the bottom plate will be shown.
```

(db21j-bottom-assembly-step-3)=
### Step 3

Screw the IMU PCB onto the top side of the bottom plate using two `N2.5x12` screws and two `N2.5` nuts as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_03.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-03
:alt: DB21J Duckiebot assembly, step 3.
```

(db21j-bottom-assembly-step-4)=
### Step 4

```{seealso}
If your omnidirectional wheel does not look like this one and is made of plastic instead of metal, follow the instructions at: [](assembly-instructions-db21j-v3) and then continue here from [Step 6](db21j-bottom-assembly-step-6).
```

Screw two `FF3x25` standoffs onto the top side of the omni wheel using two `M3x8` screws as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_04.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-04
:alt: DB21J Duckiebot assembly, step 4.
```

```{tip}
For this step and [](db21j-bottom-assembly-step-5), try using shorter screws if the suggested screws do not fully insert into the standoffs.
```

(db21j-bottom-assembly-step-5)=
### Step 5

Screw the standoffs from [](db21j-bottom-assembly-step-4) onto the bottom side of the bottom plate using two `M3x8` screws as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_05.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-05
:alt: DB21J Duckiebot assembly, step 5.
```

(db21j-bottom-assembly-step-6)=
### Step 6

Place four `M3` nuts into the bottom plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_06.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-06
:alt: DB21J Duckiebot assembly, step 6.
```

```{tip}
Occasionally, manufacturing tolerances (on the nut and the chassis) may prevent a flush fit.
Try using a different nut or changing its orientation to solve this problem.
It may also be convenient to use pliers.
```

(db21j-bottom-assembly-step-7)=
### Step 7

Connect a motor cable to a motor as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_07.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-07
:alt: DB21J Duckiebot assembly, step 7.
```

(db21j-bottom-assembly-step-8)=
### Step 8

Substeps:

1. Place the motor from [](db21j-bottom-assembly-step-7) onto the bottom left side of the bottom plate as shown below.

2. From the front side of the bottom plate, feed the motor cable from [](db21j-bottom-assembly-step-7) between the standoffs from [](db21j-bottom-assembly-step-4) as shown below.

3. From the bottom side of the bottom plate, feed the motor cable through the back left slot in the bottom plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_08.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-08
:alt: DB21J Duckiebot assembly, step 8.
```

(db21j-bottom-assembly-step-9)=
### Step 9

Screw a bottom side plate onto the left side of the bottom plate using two `M3x12` screws and two `M3` nuts from [](db21j-bottom-assembly-step-6) as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_09.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-09
:alt: DB21J Duckiebot assembly, step 9.
```

### Step 10

Substeps:

1. From the top side of the bottom plate, feed a motor support through the middle left slot in the bottom plate as shown below.

2. Screw the motor onto the left side of the motor support and right side of the bottom side plate from [](db21j-bottom-assembly-step-9) using two `M3x30` screws and two `M3` nuts as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_10.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-10
:alt: DB21J Duckiebot assembly, step 10.
```

(db21j-bottom-assembly-step-11)=
### Step 11

Connect the other motor cable to the other motor as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_11.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-11
:alt: DB21J Duckiebot assembly, step 11.
```

### Step 12

Substeps:

1. Place the motor from [](db21j-bottom-assembly-step-11) onto the bottom right side of the bottom plate as shown below.

2. From the front side of the bottom plate, feed the motor cable from [](db21j-bottom-assembly-step-11) between the standoffs from [](db21j-bottom-assembly-step-4) as shown below.

3. From the bottom side of the bottom plate, feed the motor cable through the back right slot in the bottom plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_12.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-12
:alt: DB21J Duckiebot assembly, step 12.
```

(db21j-bottom-assembly-step-13)=
### Step 13

Screw the other bottom side plate onto the right side of the bottom plate using two `M3x12` screws and two `M3` nuts from [](db21j-bottom-assembly-step-6) as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_13.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-13
:alt: DB21J Duckiebot assembly, step 13.
```

### Step 14

Substeps:

1. From the top side of the bottom plate, feed the other motor support through the middle right slot in the bottom plate as shown below.

2. Screw the motor onto the right side of the motor support and left side of the bottom side plate from [](db21j-bottom-assembly-step-13) using two `M3x30` screws and two `M3` nuts as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_14.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-14
:alt: DB21J Duckiebot assembly, step 14.
```

(db21j-bottom-assembly-step-15)=
### Step 15

Substeps:

1. Place a spacer onto each motor axle such that the spacer sits flush against the motor housing as shown below.

2. Place a wheel onto each motor axle such that the wheel sits flush against the respective spacer as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_15.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-15
:alt: DB21J Duckiebot assembly, step 15.
```

(db21j-bottom-assembly-step-16)=
### Step 16

Place two `M3` nuts into the bottom plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_16.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-16
:alt: DB21J Duckiebot assembly, step 16.
```

### Step 17

Place the Duckiebattery separator into the slots in the bottom plate and bottom side plates as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_17.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-17
:alt: DB21J Duckiebot assembly, step 17.
```

(db21j-bottom-assembly-step-18)=
### Step 18

```{attention}
Remove any USB cables connected to the Duckiebattery.
```

Place the Duckiebattery onto the top sides of the motor supports and the screws that are attaching the standoffs from [](db21j-bottom-assembly-step-4) to the bottom plate as shown below (the Duckietown logo should face away from the bottom plate).

```{figure} ../../_images/assembly/db21j/db21-rev1-step_18.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-18
:alt: DB21J Duckiebot assembly, step 18.
```

```{attention}
Verify that every component other than the cables, omni wheel sphere and motor axles is fixed.
Otherwise, gently tighten the screws of the loose components.
```

(db21j-computation-unit)=
## Computation unit

This section describes the steps to assemble the *computation unit*.

```{figure} ../../_images/assembly/db21j/db21-rev1-overview-step_19-27.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-overview-step-19-27
:alt: Overview of DB21J Duckiebot computation-unit assembly steps 19 through 27.

DB21J Duckiebot computation-unit assembly overview.
```

(db21j-computation-unit-step-19)=
### Step 19

Screw two `N2.5` nuts onto the bottom side of the Jetson Nano using two `N2.5x12` screws as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_19.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-19
:alt: DB21J Duckiebot assembly, step 19.
```

(db21j-computation-unit-step-20)=
### Step 20

Substeps:

1. Place two `M3` nuts into the middle plate as shown below.

2. Screw two `N2.5` nuts onto the top side of the middle plate using two `N2.5x12` screws as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_20.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-20
:alt: DB21J Duckiebot assembly, step 20.
```

### Step 21

Substeps:

1. Place the Jetson Nano onto the screws from [](db21j-computation-unit-step-20) as shown below.

2. Screw two `N2.5` nuts onto the bottom side of the middle plate using the screws from [](db21j-computation-unit-step-19) as shown below.

3. Screw two `MF2.5x18` standoffs onto the top side of the Jetson Nano using the screws from [](db21j-computation-unit-step-20) as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_21.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-21
:alt: DB21J Duckiebot assembly, step 21.
```

### Step 22

Screw the fan onto the heat sink of the Jetson Nano using four `M3x12` screws as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_22.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-22
:alt: DB21J Duckiebot assembly, step 22.
```

(db21j-computation-unit-step-23)=
### Step 23

Substeps:

1. Connect the red fan cable to a GPIO pin labeled `5V` on the HUT as shown below (or a GPIO pin labeled `3.3V` on the HUT for a lower fan speed and less noise).

2. Connect the black fan cable to a GPIO pin labeled `GND` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_23.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-23
:alt: DB21J Duckiebot assembly, step 23.
```

```{figure} ../../_images/assembly/db21j/db21-rev1-hut-pins.png
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-hut-pins
:alt: Pin diagram for connecting the DB21J hardware utility tool.

HUT pin assignments for the DB21J Duckiebot.
```

(db21j-computation-unit-step-24)=
### Step 24

Place four `M3` nuts into the middle plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_24.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-24
:alt: DB21J Duckiebot assembly, step 24.
```

(db21j-computation-unit-step-25)=
### Step 25

Substeps:

1. Place two `M3` nuts into the left top side plate as shown below.

2. Screw the left top side plate onto the left side of the middle plate using an `M3x12` screw as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_25.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-25
:alt: DB21J Duckiebot assembly, step 25.
```

(db21j-computation-unit-step-26)=
### Step 26

Substeps:

1. Place two `M3` nuts into the right top side plate as shown below.

2. Screw the right top side plate onto the right side of the middle plate using an `M3x12` screw as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_26.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-26
:alt: DB21J Duckiebot assembly, step 26.
```

### Step 27

From the bottom side of the middle plate, place the Duckiebattery separator and bottom side plates into the slots in the middle plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_27.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-27
:alt: DB21J Duckiebot assembly, step 27.
```

(db21j-back-assembly)=
## Back assembly

This section describes the steps to assemble the *back assembly*.

```{figure} ../../_images/assembly/db21j/db21-rev1-overview-step_28-41.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-overview-step-28-41
:alt: Overview of DB21J Duckiebot back assembly steps 28 through 41.

DB21J Duckiebot back assembly overview.
```

(db21j-back-assembly-step-28)=
### Step 28

Substeps:

1. Connect a `260 mm` JST cable to the connector on the IMU PCB as shown below.

2. From the bottom side of the middle plate, feed the cable through the front slot in the middle plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_28.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-28
:alt: DB21J Duckiebot assembly, step 28.
```

### Step 29

From the bottom side of the middle plate, feed the motor cables through the back side slots in the middle plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_29.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-29
:alt: DB21J Duckiebot assembly, step 29.
```

### Step 30

Substeps:

1. Connect the middle USB type A connector of the USB type A to USB type A and Micro USB cable to the left USB type A connector on the Duckiebattery as shown below.

2. Connect the other USB type A connector of the USB type A to USB type A and Micro USB cable to a USB type A connector on the Jetson Nano as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_30.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-30
:alt: DB21J Duckiebot assembly, step 30.
```

### Step 31

Substeps:

1. Connect the right-angled Micro USB connector of the Micro USB to Micro USB cable to the Micro USB connector on the Duckiebattery as shown below.

2. From the right side of the left top side plate, feed the cable through the back slot in the left top side plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_31.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-31
:alt: DB21J Duckiebot assembly, step 31.
```

### Step 32

Substeps:

1. Connect the USB type A connector of the USB type A to Micro USB cable to the right USB type A connector on the Duckiebattery as shown below.

2. From the right side of the right top side plate, feed the cable through the back slot in the right top side plate as shown below.

3. From the right side of the left top side plate, feed the cable through the back slot in the left top side plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_32.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-32
:alt: DB21J Duckiebot assembly, step 32.
```

(db21j-back-assembly-step-33)=
### Step 33

Connect a `120 mm` JST cable to the connector on the back bumper as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_33.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-33
:alt: DB21J Duckiebot assembly, step 33.
```

### Step 34

Substeps:

1. From the bottom side of the middle plate, feed the cable from [](db21j-back-assembly-step-33) through the left back side slot in the middle plate as shown below.

2. Screw the back bumper onto the back sides of the bottom and middle plates using three `M3x12` screws and three `M3` nuts from [](db21j-bottom-assembly-step-16) and [](db21j-computation-unit-step-24) as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_34.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-34
:alt: DB21J Duckiebot assembly, step 34.
```

### Step 35

Screw the back plate onto the back side of the top side plates using two `M3x12` screws and two `M3` nuts from [](db21j-computation-unit-step-25) and [](db21j-computation-unit-step-26) as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_35.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-35
:alt: DB21J Duckiebot assembly, step 35.
```

### Step 36

Leaving the motor cables and cable from [](db21j-back-assembly-step-33) easily accessible (for [](db21j-back-assembly-step-37), [](db21j-back-assembly-step-38) and [](db21j-back-assembly-step-39)), connect the GPIO header on the HUT to the GPIO pins on the Jetson Nano such that each GPIO pin on the Jetson Nano is in contact with its respective contact in the GPIO header on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_36.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-36
:alt: DB21J Duckiebot assembly, step 36.
```

(db21j-back-assembly-step-37)=
### Step 37

Connect the cable from [](db21j-back-assembly-step-33) to the connector labeled `LED-B` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_37.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-37
:alt: DB21J Duckiebot assembly, step 37.
```

(db21j-back-assembly-step-38)=
### Step 38

Substeps:

1. From the bottom of the HUT, feed the motor cables through the slot in the HUT as shown below.

2. Connect the left motor cable to the connector labeled `MOT-1` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_38.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-38
:alt: DB21J Duckiebot assembly, step 38.
```

(db21j-back-assembly-step-39)=
### Step 39

Connect the right motor cable to the connector labeled `MOT-2` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_39.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-39
:alt: DB21J Duckiebot assembly, step 39.
```

### Step 40

Connect the cable from [](db21j-back-assembly-step-28) to the middle connector labeled `I2C` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_40.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-40
:alt: DB21J Duckiebot assembly, step 40.
```

### Step 41

Connect the Wi-SFi dongle to a USB type A connector on the Jetson Nano as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_41.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-41
:alt: DB21J Duckiebot assembly, step 41.
```

(db21j-front-assembly)=
## Front assembly

This section describes the steps to assemble the *front assembly*.

```{figure} ../../_images/assembly/db21j/db21-rev1-overview-step_42-51.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-overview-step-42-51
:alt: Overview of DB21J Duckiebot front assembly steps 42 through 51.

DB21J Duckiebot front assembly overview.
```

### Step 42

Screw the front bumper onto the front side of the camera holder using a `N2.5x12` screw fed through the left screw hole of the camera holder and a `N2.5` nut as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_42.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-42
:alt: DB21J Duckiebot assembly, step 42.
```

(db21j-front-assembly-step-43)=
### Step 43

Screw an `MF2.5x18` standoff onto the front side of the front bumper using an `N2.5x12` screw fed through the right screw hole of the camera holder as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_43.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-43
:alt: DB21J Duckiebot assembly, step 43.
```

### Step 44

```{note}
Optionally, complete this step after [](db21j-front-assembly-step-50).
```

Screw the front bumper onto the front sides of the bottom and middle plates using three `M3x12` screws and three `M3` nuts from [](db21j-bottom-assembly-step-16) and [](db21j-computation-unit-step-24) as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_44.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-44
:alt: DB21J Duckiebot assembly, step 44.
```

### Step 45

Substeps:

1. Gently open but do not remove the/a camera cable connector on the Jetson Nano as shown below.

2. Connect the camera cable to the camera cable connector on the Jetson Nano such that the pins on the camera cable come into contact with those in the camera cable connector on the Jetson Nano as shown below (the blue strip on the camera cable should face away from the Jetson Nano).

3. Close the camera cable connector on the Jetson Nano as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_45.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-45
:alt: DB21J Duckiebot assembly, step 45.
```

```{note}
This will create a twist in the camera cable.
```

### Step 46

Screw the ToF sensor PCB onto the standoff from [](db21j-front-assembly-step-43) using an `N2.5` nut as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_46.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-46
:alt: DB21J Duckiebot assembly, step 46.
```

(db21j-front-assembly-step-47)=
### Step 47

Connect a `260 mm` JST cable to the connector on the ToF sensor PCB as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_47.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-47
:alt: DB21J Duckiebot assembly, step 47.
```

### Step 48

Substeps:

1. From the bottom side of the middle plate, feed the cable from [](db21j-front-assembly-step-47) through the front slot in the middle plate as shown below.

2. Connect the cable to the right connector labeled `I2C` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_48.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-48
:alt: DB21J Duckiebot assembly, step 48.
```

(db21j-front-assembly-step-49)=
### Step 49

Connect a `260 mm` JST cable to the connector labeled `LED-F` on the front bumper as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_49.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-49
:alt: DB21J Duckiebot assembly, step 49.
```

(db21j-front-assembly-step-50)=
### Step 50

Substeps:

1. From the bottom side of the middle plate, feed the cable from [](db21j-front-assembly-step-49) through the front slot in the middle plate as shown below.

2. Connect the cable to the connector labeled `LED-F` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_50.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-50
:alt: DB21J Duckiebot assembly, step 50.
```

### Step 51

This step has been removed.

(db21j-top-assembly)=
## Top assembly

This section describes the steps to assemble the *top assembly*.

```{figure} ../../_images/assembly/db21j/db21-rev1-overview-step_52-62.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-overview-step-52-62
:alt: Overview of DB21J Duckiebot top assembly steps 52 through 62.

DB21J Duckiebot top assembly overview.
```

(db21j-top-assembly-step-52)=
### Step 52

Substeps:

1. From the top side of the top plate, feed the top button cables through the top button hole in the top plate as shown below.

2. Screw the top button onto the top side of the top plate using the top button nut as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_52.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-52
:alt: DB21J Duckiebot assembly, step 52.
```

### Step 53

Screw the screen onto the top side of the top plate using four `N2.5x12` screws and four `N2.5` nuts as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_53.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-53
:alt: DB21J Duckiebot assembly, step 53.
```

(db21j-top-assembly-step-54)=
### Step 54

Substeps:

1. Connect the blue screen cable to the pin labeled `SDA` on the screen as shown below.

2. Connect the yellow screen cable to the pin labeled `SCL` on the screen as shown below.

3. Connect the black screen cable to the pin labeled `GND` on the screen as shown below.

4. Connect the red screen cable to the pin labeled `VCC` on the screen as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_54.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-54
:alt: DB21J Duckiebot assembly, step 54.
```

### Step 55

Connect the cable from [](db21j-top-assembly-step-52) to the connector next to the button on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_55.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-55
:alt: DB21J Duckiebot assembly, step 55.
```

### Step 56

Substeps:

1. Connect the blue cable from [](db21j-top-assembly-step-54) to the pin labeled `SDA` on the HUT as shown below.

2. Connect the yellow cable from [](db21j-top-assembly-step-54) to the pin labeled `SCL` on the HUT as shown below.

3. Connect the black cable from [](db21j-top-assembly-step-54) to the pin labeled `GND` on the HUT as shown below.

4. Connect the red cable from [](db21j-top-assembly-step-54) to the pin labeled `3.3V` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_56.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-56
:alt: DB21J Duckiebot assembly, step 56.
```

### Step 57

From the bottom side of the top plate, place the top side plates into the slots in the top plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_57.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-57
:alt: DB21J Duckiebot assembly, step 57.
```

### Step 58

Screw the top plate onto the top sides of the top side plates using two `M3x12` screws and two `M3` nuts from [](db21j-computation-unit-step-25) and [](db21j-computation-unit-step-26) as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_58.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-58
:alt: DB21J Duckiebot assembly, step 58.
```

### Step 59

Connect the Micro USB connector of the Micro USB to Micro USB cable to the connector labeled `CHARGER` `IN` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_59.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-59
:alt: DB21J Duckiebot assembly, step 59.
```

### Step 60

Connect the Micro USB connector of the USB type A to Micro USB cable to the connector labeled `5VEXT` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_60.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-60
:alt: DB21J Duckiebot assembly, step 60.
```

### Step 61

Connect the Micro USB connector of the USB type A to USB type A and Micro USB cable to the connector labeled `5VRASPI` on the HUT as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_61.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-61
:alt: DB21J Duckiebot assembly, step 61.
```

(howto-power-db21)=
## Duckiebattery

The connector labeled `OUT` `CHARGER` on the HUT will be used for charging the Duckiebattery.

```{figure} ../../_images/assembly/db21j/db21-rev1-how2charge.png
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-how2charge
:alt: Diagram showing how to charge the DB21J Duckiebattery.

Charging the DB21J Duckiebattery through the HUT.
```

```{note}
For more information on how to charge the Duckiebattery, follow [](how-to-charge-the-Duckiebattery).
```

### Step 62

The button on the Duckiebattery can be accessed through the slot in the left bottom side plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_62.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-62
:alt: DB21J Duckiebot assembly, step 62.
```

## SD card

Insert the SD card into the Jetson Nano as shown below.

```{vimeo} 527364179
```

(howto-additional-parts-db21)=
## Optional components

### Back pattern assembly

The back pattern enables the traffic management behavior used in demonstrations with other Duckiebots.

This section describes the steps to assemble the *back pattern assembly*.

### Step 63

Place the back pattern onto the back side of the back pattern plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_63.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-63
:alt: DB21J Duckiebot assembly, step 63.
```

### Step 64

Unscrew the back bumper from the back sides of the bottom and middle plates as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_64.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-64
:alt: DB21J Duckiebot assembly, step 64.
```

(db21j-optional-components-step-65)=
### Step 65

Substeps:

1. From the front side of the back bumper, feed two `M3x12` screws through the top screw holes of the back bumper as shown below.

2. Screw the back bumper back onto the back sides of the bottom and middle plates using three `M3x12` screws and three `M3` nuts from [](db21j-bottom-assembly-step-16) and [](db21j-computation-unit-step-24) as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_65.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-65
:alt: DB21J Duckiebot assembly, step 65.
```

(db21j-optional-components-step-66)=
### Step 66

Substeps:

1. Screw two `M3` nuts onto the back side of the back bumper using two `M3x12` screws from [](db21j-optional-components-step-65) as shown below.

2. Screw another `M3` nut onto each of the `M3` nuts as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_66.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-66
:alt: DB21J Duckiebot assembly, step 66.
```

### Step 67

Screw the back pattern plate onto the `M3` nuts from [](db21j-optional-components-step-66) using two `M3` nuts as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_67.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-67
:alt: DB21J Duckiebot assembly, step 67.
```

### AprilTag

The top facing AprilTag enables localization in [Duckietown Autolabs](+opmanual_autolab#book).

### Step 68

Place the AprilTag onto the top side of the top plate as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_68.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-68
:alt: DB21J Duckiebot assembly, step 68.
```

### FCC-CE sticker

Duckiebots are FCC and CE certified, meaning that they comply with (and surpass) material quality (e.g., RoHS 2.0) and electrical interference standards (FCC and CE).

### Step 69

Place the FCC-CE sticker somewhere on your Duckiebot as shown below.

```{figure} ../../_images/assembly/db21j/db21-rev1-step_69.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-rev1-step-69
:alt: DB21J Duckiebot assembly, step 69.
```

```{tip}
To prevent detection issues in more advanced applications with other Duckiebots, place the FCC-CE sticker in a location that is out of sight for those Duckiebots (e.g., under the wheels).
```

```{figure} ../../_images/assembly/db21j/db21-fcc-ce-sticker.jpg
:name: fig:assembly-instructions-duckiebot-db21j-db21-fcc-ce-sticker
:alt: FCC and CE compliance sticker placement on a DB21J Duckiebot.

An FCC-CE sticker placed under the wheels of a Duckiebot.
```

## Checkpoint

Before proceeding, make sure that:

- You have used every type of connecting component at least once, by referring to [Fig. 2](fig:db21m-rev1-parts-indices).

- Every cable is plugged in correctly but try not use force on your Duckiebot, as it is (almost) never useful and may lead to undesirable outcomes.

- The SD card is inserted into the dedicated SD card slot under the main board of the Jetson Nano (i.e., not in the adapter or in a USB connector).

Congratulations, your Duckiebot DB21J is now assembled!

(db21j-troubleshooting)=
## Troubleshooting

```{trouble}
I cannot find the blue chassis.
---
It may be under the white foam inside the Duckiebox.
Try to remove the inner packaging to access it.
```

```{trouble}
The Duckiebattery does not sit flush against the bottom plate.
---
Position the Duckiebattery to fit at an angle.
While this may make the assembly a little trickier, everything will work out in the end.
```

```{trouble}
I do not have enough screws of a specific type.
---
Every Duckiebox comes with enough screws of every type, plus spares for certain types.
You may have inadvertently used the incorrect type of screw at certain points during the assembly.
```

````{trouble}
I cannot screw the omni wheel in correctly, as the screws do not fit all the way into the standoffs.
---
Occasionally the standoffs are not fully threaded due to manufacturing inefficiencies.
Try to orientate the stand-off such the shorter threaded side faces the chassis.
Alternatively, try to use shorter screws (provided in the Duckiebox).
Otherwise, try to use two spare nuts to mitigate tolerances, as shown below.

![Spare nuts being used to mitigate tolerances between the omni wheel and stand-offs.](../../_images/assembly/db21j/db21-omni-dirtysolution.jpg)
````

```{trouble}
A component broke while I was trying to assemble my Duckiebot.
---
Certain components will not influence the functionality of your Duckiebot if broken.
However, if a broken component is influencing the functionality of your Duckiebot and you cannot fix it yourself, take a picture of the damage and email hardware@duckietown.com.
```

````{trouble}
The wheels wiggle and/or fall off the motors.
---
This may be due to manufacturing tolerances.
Try to remove the distance disks between the motors and wheels, making sure that the wheels are not touching the screws of the motor mounts.
Alternatively, screws are provided to fix the wheels to the motor axles, as shown below.
Make sure not to tighten the screws too hard, as this may add resistance to the spinning of the wheels (you can find the sweet spot by turning the wheel by hand and feeling the resistive torque).

![Screws fixing the wheels to the motor axles.](../../_images/assembly/db21j/db21-wheel-screws.jpg)
````

````{trouble}
I do not understand my Duckiebot's data and electrical connections.
---
A simplified block diagram of the data and electrical connections for your Duckiebot is shown below.

![A simplified block diagram of the data and electrical connections for a Duckiebot DB21J.](../../_images/assembly/db21j/db21-rev1-schematics-block-diagram.png)
````

```{trouble}
I have followed these instructions to the letter but there is something off that I cannot quite put my finger on.
---
You may have forgotten to put a duckie on top of your Duckiebot!
```
