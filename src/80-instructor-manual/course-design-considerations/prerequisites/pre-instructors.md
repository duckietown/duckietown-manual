```{seo}
:description: Typical prerequisites for Duckietown instructors.
:keywords: duckietown, prerequisites, professor, teaching assistant, TA, instructor, Docker, ROS, Python
```

(prerequisites-instructor)=
# Instructor background

Aside from the obvious knowledge required to teach the material, it will be helpful if the (main) instructor considers the following.  

(prerequisites-assistants)=
## Teaching Assistants

```{attention}
It is **strongly** recommended to recruit teaching assistants for your class, if possible. 
```
Working with robots is more involved than a typical class, and will require more support (despite Duckietown's best efforts to minimize the amount of support needed wherever possible!).

In a fully-fledged Duckietown class, with student projects and one robot per child, we have found that a sweet spot is roughly one TA per student group (i.e., 3-5 students), and one TA dedicated to hardware and behind-the-scenes support. 

```{tip}
While teaching assistants can be hired, hence motivated through money, we have found that there are other valuable forms of motivation, e.g.:
- **Ph. D. students** can be excellent TAs, and leverage students groups in the class to implement their research on physical hardware;
- **Postdoctoral researchers** will be happy to gain teaching experience and can support the teaching efforts by taking ownership of one or more modules (weeks) according to their expertise. Moreover, they can be valuable mentors to the students during projects (if applicable in your course).
```

(prerequisites-python)=
## Writing code in Python 

```{figure} ../../../_images/instructor-manual/dt-prelim-sw.png
:scale: 50%
:name: prerequisites-sw-fig
:alt: The Duckietown software stack uses Docker, ROS, and Python.

Duckietown's stack uses several technologies, some of which are considered prerequisites to a joyful Duckietown experience.
```

Python is a versatile programming language, amongst the most used in the world. Although it might not be the most performant for robotic applications, it strikes a good balance between simplicity to use and performance. 

All the Duckietown [notebooks and exercises](learning-experiences) as well as the [code that runs the robot](code) are written in Python. 

```{note}
To help students debug their solutions, someone on staff should be quite familiar with coding in Python. 
```

We also make extensive use of [Jupyter notebooks](https://jupyter.org/), which are interactive Python files that can be run in the browser. 

There are many resources out there to learn Python for free, e.g., 
 
- [learnpython.org](https://www.learnpython.org/). 

(This is just an example, we are not affiliated with this resource. Additional options: [additional resources](https://www.reddit.com/r/learnpython/comments/10hwp8f/where_do_i_learn_python_for_free/)).

(prerequisites-git)=
## Version control with Git 

```{todo}
review exercise workflow instructions and related repo links
```

The [workflow that we propose for completing the exercises](https://github.com/duckietown/duckietown-lx#readme) includes forking and cloning our [`duckietown-lx`](code-duckietown-lx) repository, as well as adding an upstream remote.

```{tip}
If you do not recognize terms such as _repository_, _clone_, _fork_, _merge_ and in general are not familiar with Git, [read the Duckietown pointers on using Git](version_control_with_git).
```

(prerequisites-linux)=
## Using the Linux Command Line

```{figure} ../../../_images/instructor-manual/dts-meta-example.jpg
:width: 500px
:name: linux-shell-dts
:alt: Linux terminal usage is streamlined by the Duckietown Shell.

Linux terminal usage is streamlined by the Duckietown Shell.
```

While we have made significant progress in recent years to reduce the requirement that students interact directly with the Linux terminal by introducing the [Duckietown Dashboard](sw-tools-ui-dashboard), some knowledge is still required at this stage. 

To streamline operations that would require complex terminal commands, we created the [Duckietown Shell](https://github.com/duckietown/duckietown-shell). Yet, being familiar with the fundamentals of terminal usage (`ls`, `cat`, `cd`, etc.) is needed and other notions like the Secure shell (`ssh`) may be useful for debugging. 

- To install the Duckietown Shell, follow the [DTS installation instructions](setup-dts);
- For an introduction to `ssh`, see the [Duckietown quick guide to `ssh`](secure-shell);
- for a general introduction to Linux, we recommend (while not being affiliated to) among other resources, the free [Linux Journey](https://linuxjourney.com/).

(prerequisites-docker)=
## Docker 

```{figure} ../../../_images/instructor-manual/pre-docker.png
:width: 600px
:name: docker-duckietown
:alt: Docker usage in Duckietown

Docker allows Duckietown to (a) work in very diverse environments reproducibly and (b) have seamless deployment of agents between real and virtual worlds.
```

Although at first glance it might seem redundant, we make extensive use of [Docker](https://hub.docker.com/) under the hood. 

Docker is a tool for containerization. In short, we package up code together with all of its dependencies into a "Docker image" which can be downloaded and run. 

In this way, we can guarantee (if we do things right) that the code will run properly and reproducibly regardless of the specific computing environment. 

We can also rigorously specify interfaces between containers, which enables portability in a very seamless way. This is how we can have one "agent" that can be run in many different ways, such as in the simulator, on the real robot, or in a cloud evaluation. 

You should not need to know the details about how this works as we have made every effort to abstract Docker away, but some [familiarity with the basics](preliminaries-docker-basics) may reduce your anxiety about what is happening. 

(prerequisites-ros)=
## Robot Operating System (ROS)

Similarly to Docker, although we make some effort to abstract things away in Python libraries, several of the [learning experiences](learning-experiences) leverage the ["Robot operating system"](https://ros.org/), which has become almost ubiquitous in robotics. 

ROS is a "middleware" software that acts as a _glue_ for the different components of the robot autonomy stack and provides tools for message passing, parameter tuning, and debugging among other things. 

We have some [specific resources](dtproject-ros) for getting started with ROS in the context of Duckietown. It is worth getting familiar with these (and even potentially assigning them as homework assignments for the students).

Going forward, Duckietown will support different middleware solutions, such as ROS2. For additional information on this effort, or if you would like to help, please reach out to us on Slack or at [info@duckietown.com](mailto:info@duckietown.com).