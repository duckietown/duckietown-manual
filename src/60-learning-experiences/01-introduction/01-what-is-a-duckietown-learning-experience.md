```{seo}
:description: Learn what a Duckietown LX (Learning Experience) is and how it enables robotics education through modular, interactive, and practical learning activities.
:keywords: Duckietown learning experience, LX, hands on learning, robotics education, modular curriculum, robot challenges, instructors, learners
```

(duckietown-lx)=
# What is a Duckietown LX?

```{admonition} Definition
A learning experience (LX) is a stand-alone block of activities that is self-contained and can plug and play into a full course of materials.
```

**Learners** can complete activities from the Duckietown LX library. This will allow you to dive into the fundamental topics of robotics and then immediately implement behaviors on your Duckiebot using your new skills. See [How To - Complete an LX](env-setup) to jump right in.

**Instructors** can create additional custom learning experiences using the Duckietown development tools to present course content as interactive notebooks. To cement topics in practice, you can seamlessly integrate additional robot activities and simulated challenges in a preconfigured environment. 

This prevents students from getting lost in debugging before their project even begins by eliminating extra setup steps and smoothing over complex implementation details.  You can see all available features on [](lx-features) and the LX creation tutorial in [How To - Create an LX](how-to-create-lx).

## Intended Learning Outcomes (ILOs)

Learning outcomes after completing a learning experience should generally be actionable skills to demonstrate new knowledge.  

These skills are exercised in a final activity in each LX that can be run on a virtual or real physical Duckiebot.

## Learning Goals

LX developers should answer the following questions in the LX description contained in each README. Anyone working through an LX should use this information to direct their efforts as they choose and work through LX:

```{list-table}
:header-rows: 1
:name: learning-goals-tab
* - Question
  - Example
* - What will the LX learner gain from this experience? 
  - Learners will be able to describe and implement a PID controller for a differential drive robot.
* - What are the output activities of the experience?
  - Learners will tune and test their PID controller on a Simulated Duckiebot to achieve a distance traveled goal.
* - What is the prerequisite knowledge and where can learners find it?
  - This LX depends on students having completed the Duckietown ROS LX for the fundamentals of using ROS messages.
```