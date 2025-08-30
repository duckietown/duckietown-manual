```{seo}
:description: Typical prerequisites for Duckietown class students.
:keywords: duckietown, prerequisites, student, learner, coding, ubuntu, terminal interface, python, docker, ROS, kinematics, algebra, calculus, probability theory
```

(prerequisites-students)=
# Student background

What you require students to know before joining your class is very much a design decision that will guide how rapidly your course can progress. 

In particular, it will affect the [learning experiences](learning-experiences) and homework assignments that the students will be able to complete. 

You may have no say in the matter, depending on your institution's dynamics, but we recommend that you at least ask students at the beginning of the course what their perceived proficiency in certain technical topics is. 

Here are a few example course introduction forms for you to take inspiration from:

- [Duckietown introduction survey - Google form](https://forms.gle/m3ycdemnbuomuaVY7)
- [Autonomous Vehicles class - Google form - University of Montreal](https://docs.google.com/forms/d/16NfbQWw5SQF11ouWQCMkOAARYM7dzuS0jzD8XdVvE2k)

In general, your life will be easier if your students have some level of computer science background, and/or are very motivated to learn.

(prerequisites-students-technical)=
## Student Technical Background

Specifics may vary significantly from department to department, e.g., mechanical engineering students might be stronger in control systems and weaker in coding with respect to their computer science peers.

Moreover, technical prerequisites will vary depending on the intended learning outcomes of the class, and in some sense on the level at which it is taught (undergraduate or graduate level). 

Here are some **technical prerequisites** that should be considered as guidelines:

* Basic coding skills and tools: 

  * **Linux/Ubuntu terminal interface**: the most complete way to interface with Duckietown is via terminal, so basic knowledge of Bash is required (`cd`, `ls`, `mkdir`, ...). Using Linux (Ubuntu) typically comes as a shock to some instructors as well as learners, but we strongly recommend throwing your heart over the obstacle and start learning. A life is not enough to learn _everything_ there is to know in Linux and we provide step-by-step instructions as well an "operating system", the [Duckietown Shell](https://github.com/duckietown/duckietown-shell) (`dts`) to streamline everything;
  
  * **Python**: We are going to write "autonomy" code in Python;
  
  * **Git/GitHub**: We are going to pull, fork, push, branch repositories, etc.

(prerequisites-students-academic)=
## Student Academic Background

You may also decide to cater the course material based on the students' previous exposure to subjects such as:

* Mathematics and Physics
  * Elements of **linear algebra**: matrices are used to represent coordinate systems;
  * Notions of **probability theory**: concepts like Bayes theorem, marginalization, probability distribution will be used to derive perception algorithms for the Duckiebot and Duckiedrone;
  * **Calculus** I: learners should be familiar with the notion of derivatives, ODEs, and ideally of their discrete equivalents (finite differences);
  * Fundamentals of **kinematics**: basic vector algebra, rotation fields, relations between position, velocity and acceleration are going to be used to derive equations of motion.