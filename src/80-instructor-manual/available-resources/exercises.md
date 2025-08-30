```{seo}
:description: Duckietown learning experiences are all-inclusive interactive "weeks of class".
:keywords: learning experience, LX, duckietown, Jupyter Notebook, activities, exercises, notes, simulation, hardware, robots, theory, practice, Python
```
(learning-experiences)=
# Activities and Exercises: Learning Experiences (LXs)

```{note}
Duckietown learning experiences (LXs) a ready-to-go "weeks" of class. They include videos, notes, interactive activities, and exercises, and are integrated with the Duckietown technical infrastructure (simulator, hardware, evaluation infrastructure).  
```

We define: 
* "activities" as learning tasks to which solutions are provided. Activities are designed to be "tutorials" for specific topics.
* "exercises" as learning tasks to which solutions are not provided. Solutions to exercises are typically matched to "challenges", which provide [evaluations of performance](evaluation) across engineering metrics. These evaluations can be leveraged to, e.g., automatically grade student assignments. 
* Duckietown "learning activities" (LX): as standalone classes on specific topics, typically containing activities, exercises, videos, slides, quizzes and pointers to further reading. LXs can be thought of as a week of (university-level) classes.

Both activities and exercises are structured to include [Jupyter Notebooks](https://jupyter.org/) that introduce a concept followed by coding blocks. For the most part, the result is a piece of code that can be easily:

 - Run in a simulation environment;
 - Run on robot hardware;
 - Submit for automatic evaluation.
 
The pedagogical goal in general is to explore some narrowly scoped component of the autonomy stack with everything else being "hidden" (or provided) so that the student may experience the impact of that component on the others. Whenever possible, the result of the exercise should be an "end-to-end" experience that makes the robot do something (e.g., move). 

For a complete description of the technical components of the learning experiences (LXs) please refer to the [Learning Experiences Manual](temp-lx-devmanual-lx-dev-intro). This includes information about the workflow for completing an exercise and the procedure for creating your own learning experience from scratch. 

For help on how to create learning experiences, [open a question on Stack Overflow with the tag `LX`](https://stackoverflow.com/questions/ask?tags=LX) (preferred), or ask on the [#help-build-lxs channel](https://duckietown.slack.com/archives/C067EHWQ09Y) on Slack.

(mooc-exercises)=
## MOOC Activities and Exercises

The [Self-driving Cars with Duckietown Massive Online Open Class](https://duckietown.com/self-driving-cars-with-duckietown-mooc/) comprises the following learning experiences. Activities and exercises can be accessed independently of the MOOC at:

```{list-table}
:header-rows: 1
:name: mooc-exercises-table
* - EXERCISE NAME
  - DESCRIPTION
* - [Braitenberg](https://github.com/duckietown/duckietown-lx/tree/mooc2022/braitenberg)
  - A very simple reactive control approach that is inspired by the repulsive and attractive forces
* - [Modeling and Control](https://github.com/duckietown/duckietown-lx/tree/mooc2022/modcon)
  - We build a kinematic model of the Duckiebot and build a simple PID controller using the feedback from the encoders
* - [Object Detection](https://github.com/duckietown/duckietown-lx/tree/mooc2022/object-detection)
  - We train a deep neural network to detect objects and connect it to the control of the Duckiebot
* - [Visual Lane Servoing](https://github.com/duckietown/duckietown-lx/tree/mooc2022/visual-lane-servoing)
  - We use basic concepts of computer vision to build a reactive control that operates directly on the camera images
* - [State Estimation](https://github.com/duckietown/duckietown-lx/tree/mooc2022/state-estimation)
  - A somewhat more advanced exercise that takes the detections of the road markings and uses them to calculate an estimate of the robot's state
* - [Collision Checker](https://github.com/duckietown/duckietown-lx/tree/mooc2022/collision-checker) 
  - We build an algorithm to detect if the robot will collide with it's environment by understanding its state and geometry
* - [Planning](https://github.com/duckietown/duckietown-lx/tree/mooc2022/planning)
  - We explore algorithms that the Duckiebot can use to successfully navigate in a cluttered environment
```



<!--(other-exercises)=
## Other Exercises
-->
