(student-projects)=
# Projects

```{seo}
:description: Hands-on projects are effective learning activities for students in a Duckietown class. Learn more about past projects and get some ideas for yours here.
:keywords: Duckietown, projects, student projects
```

Student projects can be an excellent way to cultivate good class cohesion and promote hands-on learning. 

```{figure} ../../../_images/instructor-manual/example-dt-projects-c.png
:name: example-projects
:scale: 40%
:align: center

Projects are a great way to learn by doing. Check out some examples of [past projects](https://vimeo.com/showcase/9972073).
```

<!--See the page in the next section: [](successful-projects), for some of our recommendations about how to make the project experience successful.--> 
In this page, we will outline the resources that are available to support student projects. 

(student-project-structure)=
## Project Structure

We have experimented with different models for project structure. 

One model that has worked extremely well has been to create one large overarching objective, and then break it down into sub-projects. In this way, we can create a type of "startup company" atmosphere that promotes cooperation and collective learning. Often we will assign one group to be responsible for the integration of the work of the other groups. 

A different but also very acceptable model is to allow students to work on smaller but more independent projects. 

See [](student-project-ideas) for some concrete ideas for projects. These typically revolve around the idea of improving, expanding or creating new autonomous behaviors.

In either case, it may be a good idea to present some concrete project suggestions and then ask the students to fill out a form (such as [this](https://forms.gle/Z3r1St8wqkCTJHhq8)) to indicate their interest in the various topics. 

Then, an assignment can be made that optimally allocates students to the topics that interest them the most. 


(student-report-templates)=
## Project Report Templates

If you decide to make the project groups submit progress reports, you may find the following templates a useful starting point for your students to structure their reports:

* [**Preliminary Design Report Template**](https://docs.google.com/document/d/1NiD76fUTW_4_fLucbwKaqtc7EPSdqRIy-td0xJS413M/edit?usp=sharing): Usually due about one-third of the way through the allotted period. The principal objective is for the team to converge on the topic that they will work on, how to define its success, and have some idea about its feasibility.

* [**Critical Design Report Template**](https://docs.google.com/document/d/1plhFsR8ZEF0o7uNsB63xAplFSfzomaPcO4c15oQstfc/edit?usp=sharing): Usually due about two-thirds of the way through the allotted period. The students should have converged on their project and the scope should be clear. In this document, they outline the implementation strategy and final demo/evaluation plan. 

* [**Final Report Template**](https://docs.google.com/document/d/1fhxsS3rqLjssmwj-P0E_qVtKRZmyK2iF7iulQ2M826I/edit?usp=sharing): Due at the end of the allotted time. Should detail what was achieved and document the steps to reproduce it.

(project-development-workflow)=
## Development Workflow for Projects

Although you may exclusively use the [`dts code` workflow](duckiebot-lxs) for the exercises, you may find this limiting 
for more expansive projects. The `dts code` workflow is designed specifically for learning experiences that are quite narrowly scoped and specific. 

In the context of projects, the scope may be larger and your students may need more flexibility. As a result, in general, 
we recommend that students get familiar with the [`DTProjects`](dtproject) structure. 
In particular, we have [project template](project-templates) repositories for different types of projects. 
This workflow uses the `dts devel` interface as opposed to `dts code`. 
A good place to start is [](creating-new-demos) to learn about creating demos and specifically [](dtproject-ros) if you
would like to use ROS.

 To discuss this topic you can reach out on the [#devel-dt-projects](https://duckietown.slack.com/archives/C067CHR5H8D) Slack channel.
