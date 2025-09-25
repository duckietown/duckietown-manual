```{seo}
:description: Discover the full range of activities offered in Duckietown Learning Experiences (LX), including notebooks, simulations, and robot agent interactions.
:keywords: Duckietown, learning experience, LX features, robotics education, simulation, Duckiebot, Jupyter notebook, robot agent, evaluation
```

(lx-features)=
# LX Features and Activities

Let us start by understanding each of the learning experience activities available and how they might be used.


The `duckietown-lx` repository on GitHub contains the learning experiences developed by the Duckietown team - we will
break down the [Object Detection](https://github.com/duckietown/duckietown-lx/tree/mooc2022/object-detection) LX as the main example here.

```{todo}
update once new ente LXs are released
```

```{note}
Learning Experiences are run using the `dts code` workflow as described in
the [](duckiebot-lxs) page. This command set gives students a streamlined environment and powerful tools to complete activities.
```

The following activity types can be implemented with the Duckietown Learning Experience infrastructure:

* [Notebook](notebooks-intro)
* [Workbench Tool](workbench-intro)
* [Running on a Virtual Duckiebotd](simulator-intro)
* [Running on a Real Duckiebot](agents-intro)

---

(notebooks-intro)=
## Activity: Notebooks

Learners are immediately presented with the goals and workflow instructions for a learning experience when they
use `dts code editor` to spin up the preconfigured VSCode editor. Installing a local editor is not necessary, and
everyone begins with a uniform environment to complete the learning experience. The `notebooks` directory will always
contain the first activity.

```{figure} ../_images/lx-devmanual/intro/obj-det-editor.png
:name: editor-activity-intro-1
:alt: Screenshot of notebook-based activity interface with goals and workflow
:align: center
:width: 90%

Editor interface for launching notebooks in a learning experience
```

A _notebook activity_ introduces key concepts within a Jupyter notebook that learners can work through to cement, visualize, and implement their understanding. Tab through the gallery of notebooks below for a few examples of notebook features.

`````{tab-set}
````{tab-item} Image Filtering
```{figure} ../_images/lx-devmanual/intro/vislane-notebook.png
:name: notebook-gallery-2
:alt: Jupyter notebook showing image filtering example
:align: center
:width: 90%

Image filtering LX - example activity
```
````

````{tab-item} Object Detection
```{figure} ../_images/lx-devmanual/intro/obj-det-notebook.png
:name: notebook-gallery-3
:alt: Jupyter notebook with object detection model output
:align: center
:width: 90%

Object Detection LX - example activity
```
````

````{tab-item} Hello World
```{figure} ../_images/lx-devmanual/intro/hello-world-notebook.png
:name: notebook-gallery-1
:alt: Basic Hello World notebook setup
:align: center
:width: 90%

Hello World LX - example activity
```
````
`````

Learners may also be directed to implement long-form solutions in the provided `solution` package. This code can be imported to notebooks for visualization and testing or used by an agent node on the Duckiebot.

```{figure} ../_images/lx-devmanual/intro/obj-det-solution.png
:name: notebook-solution
:alt: Screenshot of the solution folder showing implementation files
:align: center
:width: 90%

Example solution structure
```

### Providing Guidance

Students should be given instruction within the notebooks on how to progress through the LX activities in order.
Every learning experience should also revolve around a main _Learning Goal_ (or set of learning goals), documented at the beginning of the
`README` file.

```{admonition} Example Learning Goal
The Object Detection learning experience will take you through the process of collecting data from the Duckietown simulator and formatting it to be used to train a neural network to perform object detection using the robot's camera image. We will use one of the most popular object detection neural networks, called YOLO (v5). Finally you will integrate this trained model into the autonomy stack to create a Duckiebot agent that stops whenever an object (duckie) is detected in the road.
```

---

(workbench-intro)=
## Activity: Workbench

A _workbench activity_ provides a VNC that is used for running tools, simulation, and agent-based activities.
This is a fully functional Desktop environment with the Duckietown and ROS dependencies installed and can be started by
simply running `dts code workbench`. Instructors can develop custom tools or incorporate any standard ROS tool into
the LX activity.

The object detection LX uses the workbench environment to run a dataset augmentation tool for learners.

```{figure} ../_images/lx-devmanual/intro/obj-det-workbench.png
:name: workbench-activity-intro-1
:alt: Dataset augmentation tool running in Duckietown workbench
:align: center
:width: 90%

Workbench environment enables development of various tools, e.g., for running dataset augmentation for object detection
```

It can also be used to display the object detection model results as applied to an image stream from the Duckiebot
for visual analysis.

```{figure} ../_images/lx-devmanual/intro/workbench-detector.jpeg
:name: workbench-activity-detector
:alt: Object detection visual output inside workbench environment
:align: center
:width: 80%

Object detection visual output inside dts workbench environment
```

---

(simulator-intro)=
## Running Code in Simulation

The workbench can also run simulated (virtual) Duckiebot agents, allowing learners to test their robot behaviors in a
virtual environment.

```{figure} ../_images/lx-devmanual/intro/workbench-sim-view.png
:name: sim-activity-intro
:alt: Simulated Duckiebot running in Duckietown environment
:align: center
:width: 90%

Workbench simulation for Duckiebot agent
```

---

(agents-intro)=
## Running Code on Duckiebot

Once their solution works in simulation, learners may wish to run their solution on a real-world Duckiebot in a
Duckietown environment like the one shown below.

```{figure} ../_images/lx-devmanual/intro/duckiebot-env.jpg
:name: duckiebot-env
:alt: Real Duckiebot in a Duckietown environment
:align: center
:width: 90%

DB21J4 Duckiebot in a physical Duckietown
```

The _workbench_ can interface with the Duckiebot using the ROS network and run connected tools such as keyboard control
or `rviz`. Tab through the gallery below to see examples of a variety of tools for interacting with Duckiebot agents.

`````{tab-set}
````{tab-item} Image Streams
```{figure} ../_images/lx-devmanual/intro/obj-det-duckiebot.png
:name: workbench-gallery-1
:alt: Image stream view of object detection on Duckiebot
:align: center
:width: 90%

Live Duckiebot image stream with detection overlay
```
````

````{tab-item} Rviz and Custom Tools
```{figure} ../_images/lx-devmanual/intro/workbench-rviz.png
:name: workbench-gallery-2
:alt: Rviz visualization in Duckietown workbench
:align: center
:width: 90%

Rviz environment in workbench
```
````

````{tab-item} Keyboard Control
```{figure} ../_images/lx-devmanual/intro/workbench-joystick.png
:name: workbench-gallery-3
:alt: Joystick control interface for Duckiebot
:align: center
:width: 90%

Workbench keyboard control interface for Duckiebot
```
````
`````