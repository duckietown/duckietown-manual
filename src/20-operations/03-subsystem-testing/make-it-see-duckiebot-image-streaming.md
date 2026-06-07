(ops-db-subsys-make-it-see)=
# Image Streaming (Make it See!)


```{seo}
:description: How to access the Duckiebot camera stream (or, see what it sees).
:keywords: Duckietown, Duckiebot, camera stream, perception, image sensing, duckietown image viewer
```

This section describes how to see access the Duckiebot's camera stream. Three methods are shown, one to access the images as the Duckiebot sees them, and two to access images as humans see them.

```{needget}
- A correctly assembled Duckiebot: [](db-testing-hw-components)
- (for most methods) A functional DTS installation: [](setup-dts)
---
- Seeing images as the Duckiebot sees them
- Knowledge on the Duckietown image viewer
```

(ops-db-subsys-make-it-see-image-viewer)=
## The Duckietown Image Viewer

One of the easiest ways to see your Duckiebot's camera stream is by using the `Image Viewer`.

```{figure} ../../_images/software_tools/image_viewer/image_viewer.png
:name: image_viewer
:align: center
:width: 60%
:alt: the Duckietown image viewer enables basic user camera operations such as viewing the image stream and capturing a frame to disk

The Duckietown "Image Viewer" helps visualize the Duckiebot's camera stream.
```

:::::{tab-set}

::::{tab-item} Ubuntu

To open the `Image Viewer`, first make sure you can successfully ping the Duckiebot with `ping ROBOT_NAME.local`, then run:

```shell
dts duckiebot image_viewer ROBOT_NAME
```

where `ROBOT_NAME` is the hostname of either a physical or virtual Duckiebot.  

::::

::::{tab-item} Duckietown Workspace

There are two ways to open the `Image Viewer`: 

1. If you have installed `dts` on the host machine: open a terminal on your host machine and run:

    dts duckiebot image_viewer ROBOT_NAME

```{note}
The first time a robot app is ran, a popup window may appear asking for permissions. Insert your password and "(Always) Allow" to continue. 
```

2. Alternatively, inside the Workspace terminal run:

    dts duckiebot image_viewer ROBOT_NAME --browser

where `ROBOT_NAME` is the hostname of either a physical or virtual Duckiebot.  

::::
:::::

<!--
```{note}
{{ dt_workspace_duckietown_viewer_note.format(dt_workspace_note_prefix, "image_viewer") }}
```
-->

Note the keys in the table below.

```{list-table}
:header-rows: 1
:name: table:image-viewer-commands

* - Key
  - Function
* - <kbd>X</kbd>
  - Increase the `Frame Rate`
* - <kbd>Z</kbd>
  - Decrease the `Frame Rate`
* - <kbd>Space</kbd>
  - Capture an image
* - <kbd>R</kbd>
  - Refresh the window
* - <kbd>T</kbd>
  - Open the `Debug Console`
```

(ops-db-subsys-make-it-see-dashboard)=
## Through the browser: the Duckietown Dashboard Mission Control page

After setting up the robot dashboard [](duckiebot-dashboard-setup), the image stream is accessible on the [Mission control page of your Duckiebot Dashboard](dashboard-pages-robot-mission-control). 

```{figure} ../../_images/software_tools/dashboard/dashboard_mission_control_camera_feed.png
:name: dashboard_mission_control_camera_feed
:align: center
:width: 60%
:alt: the Duckietown dashboard mission control page showing the duckiebot's camera stream

The Dashboard Robot > Mission Control page shows basic sensor and actuator data streams.
```

By default, the camera stream in the Dashboard is throttled down to 8 frames per second. This is to minimize the resources used by your browser while streaming images from the robot, and it is not representative of the actual streaming frequency of images (which should be between 20-30Hz). Feel free to increase the data stream frequency in the **Properties** tab of the camera block.

```{tip}
If you see a black image in the camera block, or background noise, make sure that you removed the protective cap that covers the camera lens of your Duckiebot.
```

```{attention}
There is a known bug for which the image stream will flicker when using Mozilla Firefox. Change browser, e.g., to Chrome bypass this.
```

```{note}
Virtual Duckiebots will not show any image unless they are attached to a Duckiematrix engine.
```


(view-image-using-rqt-image-view)=
## Viewing the Image Stream on Your Laptop through `rqt image view`

The camera image is streaming from your Duckiebot by default on startup.

To see it, open a terminal and run:

    dts gui ROBOT_NAME

This will start a container with access to the ROS topics, messages and parameters of the Duckiebot, including the image stream from the camera.

Your terminal has now turned into a command line interface running inside of that container within the Duckiebot. You can exit the container back to your normal terminal interface at any time by running the `exit` command.

<!--
You will learn more about this tool in the [Operation - Tools](ops-tools) section.
-->

To view the camera stream, run:

    rqt_image_view

The command will open a window where you can view the image.

You will have to select the `camera_node/image/compressed` topic from the drop-down menu:

```{figure} ../../_images/software_tools/image_viewer/rqt_image_view.png
:name: rqt_dropdown_sub
:align: center
:width: 60%
:alt: rqt image view window with dropdown menu in duckietown

The rqt image view window with dropdown menu - select the `camera_node/image/compressed` topic.
```

(save-image-using-rqt-image-view)=
### How to save a picture from `rqt_image_view`

On the top right of the `rqt_image_view` window, there is a button to save the current frame to an image. But do not save it yet. A little extra setup is needed to be able to view that file later.

Create a folder on you laptop for where you would like to have the image saved to, say `~/duckiebot_images/`. Then, launch the `gui` with the following command:

```
dts gui --mount ~/duckiebot_images/:/duckiebot_images [DUCKIEBOT_NAME]
```

Then, run `rqt_image_view` again, and use the top-right "**Save as image**" button to save to the `/duckiebot_images` folder. To find that folder, you might need to navigate to `Computer` and select `/` directory in the pop-up dialogue.

```{image} ../../_images/software_tools/image_viewer/rqt_image_view_save_btn.png
:align: center
:name: rqt_save_btn
```

<br/>

```{image} ../../_images/software_tools/image_viewer/rqt_image_view_save_dialog1.png
:align: center
:name: rqt_save_dialog1
:width: 60%
:alt: rqt image view saving an image step 1

```

<br/>

```{image} ../../_images/software_tools/image_viewer/rqt_image_view_save_dialog2.png
:align: center
:name: rqt_save_dialog2
:width: 60%
:alt: rqt image view saving an image step 2
```

<br/>

And the saved image from your robot's view should appear in the folder you created!

(view-image-echo-rostopic)=
### How to see images as the robot sees them

While in the `gui tools` terminal, run:

    rostopic list

If using the baseline ROS image from Duckietown, you will see list of ROS topics. Without getting in the details of ROS at this stage (check the [learning experiences](duckiebot-lxs) for additional information), you will find a topic named `TOPIC_NAME` with `camera_node/image/compressed` in it. Run:

    rostopic echo TOPIC_NAME

to see the data (messages) being transmitted over that channel (topic). Press <kbd>CTRL-C</kbd> to stop the stream and go back to the terminal.

(operation-make-it-see-troubleshooting)=
## Troubleshooting

```{trouble}
I can see messages being sent from my Duckiebot when looking at the `DUCKIEBOT_NAME/sensor/camera/front_center/jpeg` `DTPS` topic, after following [](sw-tools-dtps), but I do not see an image.
---
Make sure that the `duckiebot-interface` container is running by checking the `Portainer` page of the `Dashboard` (opened by running `dts duckiebot dashboard DUCKIEBOT_NAME --page portainer`) or by running:

    `docker -H DUCKIEBOT_NAME.local ps`

The exact name of the container will depend on your Duckiebot's version. If you do not see the `duckiebot-interface` container, update your Duckiebot by running:

    `dts duckiebot update DUCKIEBOT_NAME`
```

```{trouble}
I cannot see an image after refreshing the window and I cannot see messages being sent from my Duckiebot when looking at the `DUCKIEBOT_NAME/sensor/camera/front_center/jpeg` `DTPS` topic, after following [](sw-tools-dtps).
---
Contact support.
```

```{trouble}
I see a black image.
---
Make sure that the protective cap for your Duckiebot's camera lens has been removed.
```

```{trouble}
I see an extremely noisy image.
---
Make sure that the protective cap for your Duckiebot's camera lens has been removed.
```


```{trouble}
The images are out of focus.
---
The focus for your Duckiebot's camera can be manually adjusted by rotating the mechanical focus ring on the lens. When dealing with hardware, exercise care and minimize the use of force. Occasionally, cameras come with the lens glued in place. If the lens does not rotate, you may need to break the glue.
```
