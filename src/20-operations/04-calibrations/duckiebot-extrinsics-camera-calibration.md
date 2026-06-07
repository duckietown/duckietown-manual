```{seo}
:description: Learn how to perform the extrinsics camera calibration procedure for a Duckietown Duckiebot. Extrinsics calibration identifies the spatial relation between the camera and robot frames. 
:keywords: Duckiebot, calibration, camera calibration, extrinsics camera calibration
```

```{needget}
- A working Duckiebot: [](ops-db-subsys-testing-intro)
- A functional `dts` installation: [](setup-dts)
- A camera calibration pattern, e.g., as provided in a Duckiebox.
---
- A Duckiebot with the extrinsics camera calibration performed.
```

(operation-camera-extrinsic-calibration)=
# Extrinsic camera calibration procedure

This camera calibration procedure outputs the relative pose between the camera and Duckiebot frame.

For optimal performance, repeat this procedure if you ship the Duckiebot or otherwise touch the camera holder.

## The Extrinsics Calibrator

The easiest way to perform the extrinsic camera calibration procedure for your Duckiebot is by using the `Extrinsics Calibrator`.

```{figure} ../../_images/calibrations/camera/extrinsics_calibrator_1.png
:width: 70%
:align: center
:alt: Duckietown extrinsics camera calibration interface
:name: extrinsics_calibrator_1

The `Extrinsics Calibrator`.
```

To open the `Extrinsics Calibrator`, run:

```shell
dts duckiebot calibrate_extrinsics DUCKIEBOT_NAME
```

```{note}
{{ dt_workspace_duckietown_viewer_note.format(dt_workspace_note_prefix, "calibrate_extrinsics") }}
```

Note the keys in the table below.

```{list-table}
:header-rows: 1
:name: table:extrinsics-calibrator-commands

* - Key
  - Function
* - <kbd>X</kbd>
  - Increase the `Frame Rate`
* - <kbd>Z</kbd>
  - Decrease the `Frame Rate`
* - <kbd>Space</kbd>
  - Calibrate the camera
* - <kbd>F</kbd>
  - Toggle the `Project` switch
* - <kbd>E</kbd>
  - Toggle the `Check error` switch
* - <kbd>R</kbd>
  - Refresh the window
* - <kbd>T</kbd>
  - Open the `Debug Console`
```

## Extrinsic calibration procedure

To perform the extrinsic calibration procedure:

1. (optional) Click the `Check error` switch to enforce a pose error bound for your Duckiebot's camera based on its known intrinsic parameters (a trapezoid in the image under `Camera View` should appear).
2. Position your Duckiebot on the calibration board such that it faces the checkerboard pattern, your Duckiebot's axle is parallel to and directly above the **large** `y`-axis of the calibration board, and the axis that is perpendicular to and midway between your Duckiebot's axle is directly above the **large** `x`-axis of the calibration board (if the `Check error` switch is set to `on`, the trapezoid in the image under `Camera View` should turn from black to blue).
3. Click the `Calibrate` button.
4. Wait for the spinner to disappear.
5. (optional) Click the `Project` switch to see a top-down view of what your Duckiebot sees under `Projection`.

```{figure} ../../_images/calibrations/camera/extrinsics-calibration-setup.jpg
:width: 70%
:align: center
:alt: Duckiebot extrinsics camera calibration setup
:name: extrinsic_setup


Extrinsic calibration setup: align the Duckiebot with the marks on the calibration pattern, on a white backdrop.
```

```{figure} ../../_images/calibrations/camera/extrinsics_calibrator_2.png
:width: 70%
:align: center
:alt: Duckietown extrinsics camera calibration check error function
:name: extrinsics_calibrator_2

The Extrinsics Calibrator with the Check error switch set to `on`.
```

```{figure} ../../_images/calibrations/camera/extrinsics_calibrator_3.png
:width: 70%
:align: center
:alt: Duckietown extrinsics camera calibration projection functionality
:name: extrinsics_calibrator_3

The Extrinsics Calibrator with the Project switch set to `on`.
```

To confirm that a new extrinsic calibration file has been created on your Duckiebot, run the following command and inspect the contents of the `Camera Extrinsic` panel:

```shell
dts duckiebot dashboard DUCKIEBOT_NAME --page robot/calibrations
```

```{figure} ../../_images/calibrations/camera/camera_extrinsic_panel.png
:width: 70%
:align: center
:alt: Duckietown extrinsics camera calibration extrinsics panel
:name: camera_extrinsic_panel

The `Camera Extrinsic` panel on the `Robot` page of the `Dashboard`.
```

```{note}
Within the `Camera Extrinsic` panel, under `Local`, you should see a tick next to `Completed`, the calibration date next to `Calibration date` and `/data/config/calibrations/camera_extrinsic/DUCKIEBOT_NAME.yaml` next to `Files`.
```


## Troubleshooting

```{trouble}
When I open a calibrator window, I do not see images at the center but a gray loading screen instead. I know the camera otherwise works on my Duckiebot.
---
Press the refresh icon on the top right of the calibrator window to restart the image stream.
```
