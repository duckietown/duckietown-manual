```{seo}
:description: Common pitfalls in teaching with Duckietown, and suggested solutions.
:keywords: Duckietown, pitfalls, class failure modes
```

(considerations-pitfalls)=
# Common Pitfalls

On this page, we list some common difficulties that we have experienced and some possible methods to remedy or prevent them where possible. 

## Students dropping out

Unfortunately, sometimes students do drop out of the class. This can be inconvenient, particularly if project groups have already been created because it can leave one team deficient. 

Additionally, the hardware (robot) allocated to that student may be partially constructed and it may not be possible to find another student to take the place of the one that has dropped out. It is important to consider in the design of the course that some students may drop out and that you should be able to handle such an occurrence. 

Some strategies to minimize the probability of students dropping out include:

* **Starting slowly** -  particularly with the hardware component. Some students will be more intimidated by hardware than others, and this can take time to overcome. 

One of the most likely reasons a student may drop out is because they feel they have fallen behind and they have no hope of catching up. It is also possible that there could be some problems with some hardware (it is rare, but it happens) and this can further delay students and cause frustration. 

This is the nature of working with real robots and should be embraced as much as possible. 

* **Allocate as many teaching assistant resources as possible** - in particular at the beginning of the class. Ensure that your TAs are very familiar with the hardware and software before the beginning of the class so that they can effectively help debug problems. 

* **Hide the details at the beginning** - particularly for students who have limited experience with the tools (See [](prerequisites-students)). We have structured the [learning experiences](learning-experiences) in this way deliberately. For example, the "Braitenberg" learning experience performs end-to-end control with a reactive approach that consists of simple matrix multiplication. The best approach is for the *tools* to progress in complexity at the same rate as the *complexity of the approaches* so that the necessity of the more complex tools can be appreciated. 

* **Learning to solve problems** - in some cases, things won't work properly and it will be because of a student's error or lack of understanding of the material. It can be tempting for students to blame the parts of the system that are abstracted away and that they don't understand before considering that they have made a mistake. In our experience students tend to become subject to the fallacy of imitation, or "superstition". I.e., "they had this problem and fixed by doing that thing" can lead to very frustrating rabbit holes. Presenting step-by-step debugging instructions could be useful to have students determine the actual original causes of their problems, and fix them.

* **Getting help** - in the case that there is a problem that does not seem to be related to the student's code, it can cause frustration because the student's solutions will fail, and they don't know why. 
For common problems, refer to the ["Troubleshooting Guides" in the Duckiebot operation manual](book-db-opmanual). In case the course staff needs support, refer to [](technical-support).

