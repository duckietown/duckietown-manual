```{seo}
:description: Duckietown evaluation infrastructure was developed during the AI driving olympics and provides research-grade feedback to agent submissions for specific tasks.
:keywords: Duckietown, challenge, evaluation, robot agent, ai driving olympics
```
(evaluation)=
# Evaluation

An important consideration in the construction of a class will be how the students are going to be evaluated. We typically **do not** test students' knowledge through traditional exams and tests (although this would certainly be possible). 

Instead, we recommend some combination of [exercises](learning-experiences) and a [course project](student-projects). We also typically put an above-normal emphasis on student participation or being "Being a Good Citizen" in Duckietown. 

## Evaluating Learning Experiences

An [automated evaluation system](https://challenges.duckietown.org/v4/) is available to ease the process of grading the [learning experiences](learning-experiences) in simulation.

```{figure} ../../_images/instructor-manual/challenges.png
:name: challenges-screenshot

The Duckietown "Challenges Server" is used for automated evaluation of exercise submissions
```

We have a collection of existing learning experiences that you can use in this way, or you [can design your own](temp-lx-devmanual-lx-dev-intro). 
The design of the learning experiences includes the specification of metrics that will be used to evaluate the performance of the submission to the automated evaluation system. 

We recommend that you decide on some sufficient performance and grade the submissions as either pass or fail, based on whether they have met these criteria. The reason for this is that, with careful tuning, the metrics can be optimized and overfit but this often comes with diminishing returns in terms of pedagogical value. 

It is important for students to get a flavor of how the various parameters affect the result, but when they are spending many hours tuning things, they tend to become irritated, and rightfully so. 

Also, note that we have plans to extend this capability to real robot evaluations in remote labs that we call [Autolabs](https://duckietown.com/integrated-benchmarking-and-design-for-reproducible-and-accessible-evaluation-of-robotic-agents/). Autolabs have been used, e.g., for the AI Driving Olympics, and are available in beta [upon request](mailto:hardware@duckietown.com). 

(evaluating-projects)=
## Evaluating Projects

We usually advocate for students to submit written reports and progress presentations at regular intervals. Please see the [course projects](student-projects) page for resources such as templates for these reports. 

We often solicit the students themselves to provide feedback on each others documents and presentations, to expose learners to the notion of peer review, which we believe to be more formative than traditional top-down grading. 

In our experience, it is important not to put too much weight on the final performance of the demo since this causes stress. 

(evaluating-participation)=
## Evaluating Student Participation

One of the key factors leading to a successful class experience for everyone is the ability to cultivate a sense of community and cooperation. 

Since many students are quite focused on optimizing their grades, it can be helpful to explicitly include some weight in the final evaluation for this. 

A combination of quantitative and qualitative metrics can be used to evaluate the level of participation of the students in the class. It is important to be transparent about the specific way that students will be evaluated. 

However, it is also important to express that these metrics are meant to be a guideline, or you may fall victim to [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law). 

Some metrics that we have used in the past include:

* Quantity and quality of feedback given to fellow students on reports and presentations (see [](evaluating-projects)); 
* Filing issues, fixing bugs, answering questions on Stack Overflow, making pull requests or other quantifiable contributions to the code infrastructure;
* Quality and quantity of involvement on the course communication board (Slack, etc.). 
* It can be interesting to allow students to nominate others in the class that they feel have been particularly helpful. If following this approach, make sure to require a detailed justification otherwise students may tend to only nominate their friends. Any sort of academic dishonesty (e.g., providing biased peer review because of a conflict of interests) should be penalized.

Finally, there can be some part of the participation grade that is entirely subjective and up to the discretion of the professor and/or teaching assistants. 


