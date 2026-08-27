```{seo}
:description: Discover the full range of activities offered in Duckietown Learning Experiences (LX), including notebooks, simulations, and robot agent interactions.
:keywords: Duckietown, learning experience, LX features, robotics education, simulation, Duckiebot, Jupyter notebook, robot agent, evaluation
```

(lx-overview)=
# Overview of `ente` LXs

[Currently supported `ente` learning experiences for Duckiebots](ente-supported-lxs) share a common structure and features.

Each LX is hosted in a set of repositories in the [Duckietown organization GitHub](https://github.com/duckietown). The names of these repositories follow the following structure, where `LXNAME` is the LX name: 

- `lx-[LXNAME]`: this is the "front-end" of the LX, starting point of each LX for learners. These repos are public.
- `lx-recipe-[LXNAME]`: this is the "technical backend" for each LX. These repos are public.
- `lx-[LXNAME]-solution`: this is a copy of the `lx-[LXNAME]` repo, with solutions. These repos are private, and only made available to instructors.

```{warning}
Learning experiences in daffy were structured [in a monolitic repo](https://github.com/duckietown/duckietown-lx). For additional information, refer to the [daffy Duckiebot Operation Manual](https://docs.duckietown.com/daffy/opmanual-duckiebot/lx/supported/general_running_lx.html). Note that daffy LXs are not compatible with an ente environment, and viceversa.
```


(lx-features)=
## LX Features and Activities

<!--
To explore the structure of an LX, we brake down, e.g., the [Extended Kalman Filter - Localization](https://github.com/duckietown/lx-ekf-localization) LX as the main example here.
-->

```{note}
Learning Experiences are run using the `dts code` workflow as described in: [](duckiebot-lxs). 
```

The following activity types can be implemented with the Duckietown Learning Experience infrastructure:

* [Notebook](notebooks-intro)
* [Workbench Tool](workbench-intro)
* [Running on a Virtual Duckiebot](simulator-intro)
* [Running on a Real Duckiebot](agents-intro)

---

(notebooks-intro)=
## Activity: Notebooks

Duckietown learning experiences are consumed through Notebooks, without the need to install a local editor. This offers learners a uniform experience to engage with the content. A preconfigured VScode editor and notebooks are initialized through the command:

    dts code editor

The `notebooks` directory will always contain the first activity.

```{figure} ../_images/lx-devmanual/intro/obj-det-editor.png
:name: editor-activity-intro-1
:alt: Screenshot of notebook-based activity interface with goals and workflow
:align: center
:width: 90%

Editor interface for launching notebooks in a learning experience
```

Notebooks provide a rich environment to implement learning activities, from simple text, to images and videos, interactive code cells, and much more. In Duckietown LXs, we mostly intend these notebooks as "class notes" rather than full standalone learning modules, and as preconfigured interactive coding evironment that ienable learners to focus on the intended learning outcomes of the LX rather than getting distracted by the many underlying details of robotics. 

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

(notebooks-coding)=
## Coding inside notebooks

While short form coding learning activities can be well implemented in cells, directly inside the Jupyter notebook, inside a LX learners may also be directed to implement long-form code solutions in the provided `solution` package. 

The code placed inside this folder can then be imported in the notebooks for visualization and testing, or automatically compiled and configured to be deployed as an **agent** on Duckietown robots (Duckiebot, Duckiedrones) - both physical and virtual. Code is built using the `dts code build` function:


```{figure} ../_images/lx-devmanual/intro/obj-det-solution.png
:name: notebook-solution
:alt: Screenshot of the solution folder showing implementation files
:align: center
:width: 90%

Example solution structure
```

Each learning experience typically collects more than one notebook. Starting from the first one, notebooks should be written/engineered to guide learners through the rest of the learning experience in proper order. 

<!--
### Providing Guidance

Students should be given instruction within the notebooks on how to progress through the LX activities in order.
Every learning experience should also revolve around a main _Learning Goal_ (or set of learning goals), documented at the beginning of the `README` file.

```{admonition} Example Learning Goal
The Object Detection learning experience will take you through the process of collecting data from the Duckietown simulator and formatting it to be used to train a neural network to perform object detection using the robot's camera image. We will use one of the most popular object detection neural networks, called YOLO (v5). Finally you will integrate this trained model into the autonomy stack to create a Duckiebot agent that stops whenever an object (duckie) is detected in the road.
```
-->
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