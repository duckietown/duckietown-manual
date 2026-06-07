```{seo}
:description: Learn how to perform the intrinsics camera calibration procedure for a Duckietown Duckiebot with step by step instructions. The instrinsics calibration procedure identifies parameters necessary to relate 2D image plane features to the 3D world.
:keywords: Duckiebot, calibration, camera calibration, intrinsics camera calibration
```

```{needget}
- A working Duckiebot: [](ops-db-subsys-testing-intro)
- A functional `dts` installation: [](setup-dts)
- A camera calibration pattern, e.g., as provided in a Duckiebox.
---
- A Duckiebot with the extrinsics camera calibration performed.
```

(operation-camera-intrinsic-calibration)=
# Intrinsic camera calibration

The instrinsic camera calibration procedure identifies parameters that enable creating a relationship between the 2D image plane and the 3D world around the Duckiebot. These parameters account for various optical specifications such as the camera's focal length, the pixel aspect ratio, and the distortion field applied by the fisheye lens.

```{tip}
For optimal performance, repeat this procedure if you change the focus of the camera by rotating the lens.
```

(db-instrinsics-calibrator)=
## The Intrinsics Calibrator

:::::{tab-set}

::::{tab-item} Ubuntu

To perform the intrinsic camera calibration procedure for your Duckiebot, run:

```shell
dts duckiebot calibrate_intrinsics ROBOT_NAME
```

where `ROBOT_NAME` is the hostname of either a physical or virtual Duckiebot. 
::::

::::{tab-item} Duckietown Workspace

There are two ways to perform the intrinsic camera calibration procedure for your Duckiebot:

1. If you have installed `dts` on the host machine: open a terminal on your host machine and run:

    dts duckiebot calibrate_intrinsics ROBOT_NAME

```{note}
The first time a robot app is ran, a popup window may appear asking for permissions. Insert your password and "(Always) Allow" to continue. 
```

2. Alternatively, inside the Workspace terminal run:

    dts duckiebot calibrate_intrinsics ROBOT_NAME --browser

where `ROBOT_NAME` is the hostname of either a physical or virtual Duckiebot.  

::::

:::::



<!--
```{note}
{{ dt_workspace_duckietown_viewer_note.format(dt_workspace_note_prefix, "calibrate_intrinsics") }}
```
-->

```{figure} ../../_images/calibrations/camera/intrinsics_calibrator_1.png
:width: 70%
:align: center
:alt: Duckietown instrinsics camera calibration interface
:name: intrinsics_calibrator_1

The Duckietown intrinsics camera calibration interface.
```

Note the keys in the table below.

```{list-table}
:header-rows: 1
:name: table:intrinsics-calibrator-commands

* - Key
  - Function
* - <kbd>X</kbd>
  - Increase the `Frame Rate`
* - <kbd>Z</kbd>
  - Decrease the `Frame Rate`
* - <kbd>Space</kbd>
  - Calibrate the camera
* - <kbd>F</kbd>
  - Toggle the `Undistort` switch
* - <kbd>R</kbd>
  - Refresh the window
* - <kbd>T</kbd>
  - Open the `Debug Console`
```

## Intrinsic calibration procedure

To perform the intrinsic calibration procedure:

1. Move the calibration pattern in front of your Duckiebot's camera such that the **entire** checkerboard pattern is within its field of view and colored lines begin to overlay the checkerboard pattern.
2. Rotate the mechanical focus ring on the lens until you can clearly read the `x` and `y` labels on the checkerboard pattern (do not adjust the focus again or place the lens cover back onto the lens unless you plan on repeating this procedure).
3. Slowly move the calibration board left, right, up, down, forwards and backwards, relative to your Duckiebot's camera, until each region within the `x`, `y` and `Size` bars is filled in.
4. Slowly tilt and pan the calibration board, relative to your Duckiebot's camera, until each region within the `Skew` bar is filled in.
5. Click the `Calibrate` button.
6. Wait for the spinner to disappear.
7. (optional) Click the `Undistort` switch to see an undistorted view of what your Duckiebot sees.

```{figure} ../../_images/calibrations/camera/intrinsics_calibrator_2.png
:width: 70%
:align: center
:alt: Duckietown instrinsics camera calibration interface showing a successful procedure
:name: intrinsics_calibrator_2

The Duckietown intrinsics camera calibration interface (Intrinsics Calibrator) with all of its bars filled in.
```

```{figure} ../../_images/calibrations/camera/intrinsics_calibrator_3.png
:width: 70%
:align: center
:alt: Duckietown instrinsics camera calibration interface showing a successful procedure
:name: intrinsics_calibrator_3

The `Intrinsics Calibrator` with the `Undistort` switch set to `on`.
```

To confirm that a new intrinsic calibration file has been created on your Duckiebot, run the following command and inspect the contents of the `Camera Intrinsic` panel:

```shell
dts duckiebot dashboard DUCKIEBOT_NAME --page robot/calibrations
```

```{figure} ../../_images/calibrations/camera/camera_intrinsic_panel.png
:width: 70%
:align: center
:alt: Duckietown instrinsics camera calibration interface showing a successful procedure
:name: camera_intrinsic_panel

The Camera Intrinsic panel on the Robot page of the Dashboard.
```

```{note}
Within the Camera Intrinsic panel, under `Local`, you should see a tick next to `Completed`, the calibration date next to `Calibration date` and `/data/config/calibrations/camera_intrinsic/DUCKIEBOT_NAME.yaml` next to `Files`.
```


## Troubleshooting

```{trouble}
When I open a calibrator window, I do not see images at the center but a gray loading screen instead. I know the camera otherwise works on my Duckiebot.
---
Press the refresh icon on the top right of the calibrator window to restart the image stream.
```
