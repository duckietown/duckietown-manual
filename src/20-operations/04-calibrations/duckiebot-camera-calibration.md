```{seo}
:description: Learn about camera calibration procedures for a Duckietown Duckiebot with step by step instructions on how to set up the necessary tools, and perform intrinsics and extrinsics.
:keywords: Duckiebot, calibration, camera calibration, camera calibration pattern
```

```{needget}
- A working Duckiebot: [](ops-db-subsys-testing-intro)
- A functional `dts` installation: [](setup-dts)
- A camera calibration pattern, e.g., as provided in a Duckiebox.
---
- A Duckiebot with the extrinsics camera calibration performed.
```

(db-camera-calibration)=
# Camera Calibration

This chapter describes how to perform the camera calibration procedure for your Duckiebot.

## Introduction to camera calibration

Every camera is unique due to manufacturing and assembly differences. Therefore, a camera calibration procedure needs to be performed to account for small manufacturing discrepancies.

This procedure involves displaying a predetermined pattern in front of the camera and using it to solve for the camera's parameters.

For more information about the mathematics behind the process, review the appropriate [learning experience](duckiebot-lxs).

<!--
 review [these slides](https://github.com/duckietown/lectures/blob/master/1_ideal/25_computer_vision/cv_calibration.pdf).
-->

(operation-camera-calibration-board)=
## Calibration board

```{figure} ../../_images/calibrations/camera/a3-calibration-pattern.png
:width: 20em
:align: center
:alt: Duckietown camera calibration pattern in A3 format
:name: a3-calibration-pattern

Duckietown camera calibration pattern.
```

If you do not already have a Duckietown calibration board:

1. Download the [Duckietown calibration pattern](https://github.com/duckietown/lib-dt-computer-vision/blob/ente/assets/extrinsics/camera_calibration_pattern_A3_rev0424.pdf)

2. Print it in **A3** format

3. Make sure the printing settings have not deformed the pattern, by measuring the features as indicated on the pattern itself

4. Fix it to a rigid planar surface that you can move around

```{note}
* The squares must have side lengths equal to **0.031 m** (**3.1 cm**). Measure this, as having the wrong size may lead to your Duckiebot crashing.
* In case your squares are not the correct size, make sure that your printer settings are set to **A3** format, with "no automatic scaling" and size set to `100%`.
```

```{warning}
If the pattern is not rigid, the calibrations should not be used. You can print on thick paper or adhere to something rigid to achieve this.
```
