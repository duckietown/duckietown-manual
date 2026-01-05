```{seo}
:description: Learn how to develop Duckietown Learning Experience (LX) activities aligned with your desired learning outcomes.
:keywords: Duckietown, learning experience, LX, activity development, Duckiebot, robotics curriculum, development tutorial, backwards design
```

(tips-building-lxs)=
# Tips for Building LXs

This page is intended to provide some design considerations when creating a learning experience.


## Intended Learning Outcomes (ILOs)

Learning outcomes after completing a learning experience should generally be actionable skills to demonstrate new knowledge.

These skills are exercised in a final activity in each LX that can be run on a virtual or real physical Duckiebot.

## Learning Goals

LX developers should answer the following questions in the LX description contained in each README.
Anyone working through an LX should use this information to direct their efforts as they choose and work through LX:

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


(lx-notebooks)=
## Notebook Activities

Notebooks offer a clean interface to provide lesson content, visualizations, and instructions for proceeding through an LX.

At the core, a Duckietown Learning Experience notebook has all the possibility of a [classic Jupyter notebook](https://docs.jupyter.org/en/latest/) but with every library and functionality from the Duckietown ecosystem added in.

```{figure} ../../_images/lx-devmanual/intro/hello-world-notebook.png
:name: challenges-server-1
:alt: Each challenge and learner submissions on the Duckietown Challenges Server
:align: center
:width: 90%

Each challenge and linked learner submissions can be found on the Duckietown Challenges Server.

```

Take a moment to explore the notebooks in the [Demo Learning Experience](https://github.com/duckietown/duckietown-lx/tree/demo-lx/demo-lx/notebooks) to see a few of the integration options.

### Edit zones

The following table contains a list of the files and directories that you may need to update to implement this type of LX activity. If you would like a full walkthrough showing how to implement notebooks, skip to the next section.

```{list-table} Edit zones
:header-rows: 1
:name: notebook-table

* - Feature
  - File Location
  - Purpose
* - Jupyter Notebook
  - ``` lx/notebooks/01_first_notebook.ipynb ```
  - Notebook files contain the knowledge portion of an LX, walking students through activities, visualizations, and
  development.
* - Learner Solution Code
  - `lx/packages/solution_module.py`
  - Python files for learner implementations should remain in the `packages` directory, with learners filling in TODOs
  as instructed by the notebooks.
* - Notebook Dependencies
  - `recipe/dependencies-apt.txt`, `recipe/dependencies-py3.txt`
  - Required libraries are built into the VSCode editor environment by including them in the `recipe` dependency files.
```

## Duckietown LX Development Guidelines

Here are some suggestions on how to leverage the LX infrastructure to build compelling experiences for your learners.

### Notebooks and packages:
**Notebooks and Packages**: As a general rule, example code and visualizations should be developed by learners directly in the notebooks.

Code for agents and other packages should instead be placed in the `packages/solutions` directory for learners to edit the respective Python files, then imported into the notebooks and unit tests.


### On solutions:
All but the last notebooks should generally be thought of as guided tutorials (or, _learning activities_), introducing the background and tools required to implement a complex autonomous behavior for the Duckiebots. The final notebook can be thought of as a _learning assessment_ instead, where users are expected to bring together and build upon the learning activities to produce their own solution. Learning assessments should not have solutions publicly available.

Learners should be editing package files during the activities to implement their work, as directed by the notebook instructions. Solutions to the activities should be provided after the students gave an honest attempt at solving them on their own.

The solution to the assessment instead should be hidden in the separate solutions repository, to enable evaluation.

### Notebook length:

The format of a Duckietown LX paired with the `dts code` workflow enables learners to iteratively edit the notebooks and execute their solution approaches to the pedagogical challenges provided, reinforcing their understanding with immediate feedback.

Within this framework, shorter notebooks with concrete goals that build learner skills up to a final agent challenge are more effective than one long, content-heavy notebook. Granularity should be preferred to monolithic LXs.

## Tutorial: Adding Content to Notebooks

### Confirm your LX workspace setup

The first step after creating a new development project should always be to run `dts code build  --recipe ../recipe` in the `<your-lx-workspace>/lx` directory, to ensure the template was initialized properly.

### Backwards design: start from the intended learning outcomes (ILOs)

What do you want your students to take away from this learning experience? Try to write it down as a skill, starting with an active verb, e.g.:

* Learners will be able to implement a PID controller once provided with the reference and output signals from a plant;
* Learners will explain the effects of changing <some parameter> of <some algorithm> to their peers using the correct terminology;

Defining the intended learning outcomes will inform the content and visualization that you add to the notebook. It helps clearly determine the scope of the learning experience, by formalizing its end.

We recommend to limit the number of ILOs for each learning experience to 3-5. When you find yourself wanting learners to take away a larger number of learning outcomes, consider breaking down your LX into multiple LXs.

### Determine the prerequisites and dependencies

Having formalized the end point of your soon-to-be LX, i.e., the ILOs, it is good practice to similarly define what are the prerequisites for engaging in this LX. Prerequisites can be:

* purely theoretical: e.g., learners should know linear algebra and ODEs before engaging in a LX designed to derive the dynamic model of a robot;
* tools related: e.g., learners should have a computer set up in a certain way, with at least tot amount of free hardware space;
* skill related: e.g., learners should have completed another LX (with skill-focused ILOs), and be familiar with how to run update a Duckiebot.

Moreover, if possible determine the required Duckietown and external libraries that you envision using during the LX, and add them to a setup cell at the beginning of the notebook. This will avoid import errors and let you focus on fleshing out the learning activities.

You can install external libraries by adding to the `recipe/dependencies-apt.txt` and `recipe/dependencies-py3.txt` files.  Any dependencies listed added here will be available in the VSCode editor environment.

### Content and Code Recommendations

Content is added to a LX notebooks in the same Markdown format as any standard Jupyter notebook.  For more information, see the [Jupyter notebook docs](https://docs.jupyter.org/en/latest/).

As noted above, students should be editing package files to implement their work as directed by the notebook instructions, and the solution should be hidden in
the separate solutions repository to enable evaluation. This means that there are three places you can choose to have learners write solution code.

1. Directly in the notebook cells. This should be used for content examples and practice.
2. In a solution Python script in the `lx/packages/solution` directory that is imported into the notebook for visualization.  All functions should be predefined with clear **TODOs** marked for learners to complete as directed by the notebook.
3. In a solution Python script in the `lx/packages/solution` directory that is then imported into the Duckiebot agent code located in the `recipe` for simulation and workbench activities (more on this in the following sections).

As a general rule, notebooks **do not** have access to the packages in the `recipe/solutions` directory where the base code is placed for Duckiebot agents.  This is to prevent learners from editing agent code to a confusing or unusable state.

**In summary:** place visualization and content practice code in the notebook. Place learner solution code in linked Python scripts housed in the solutions directory.

```{hint}

Strengthen learner test-driven development (TDD) habits by using the Testing interface in the `VSCode` editor, to provide unit tests for each function to be completed in an LX.

This will confirm that their solution performs as expected before any attempts to run it in simulation or on Duckiebots. Note that the beaker symbol to open the Testing interface may not appear in the sidebar until after one of the Python files in the `packages` directory has been opened.

```{figure} ../../_images/lx-devmanual/consume/test-interface.png
:align: center
```

### Clean up and Publish

Clear all cells of output to avoid publishing solutions. Then push your recipe and new LX repositories.
