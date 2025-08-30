```{seo}
:description: Slides and recording used to introduce planning in Duckietown. 
:keywords: Motion planning, graph search, optimal control, duckietown
```

(slides-and-recordings-planning-overview)=
# Planning


This section lists slides and recordings used to present topics related to robot planning. 

Typically, this problem is formulated as operating at a higher level of abstraction than the problem of [robot control](slides-and-recordings-control-overview). Nevertheless, a formal framework for viewing this problem is through the lens of optimal control. 

This formulation is theoretically interesting, but often impractical unless significant approximations are made. An alternative is to formulate the planning problem as some kind of search over graphs. There are several different approaches to do this, but then we can leverage well-known methods of graph search to find the optimal plan (or a good approximation to it). 

For the accompanying exercise, see [Planning](mooc-exercises).

```{tableofcontents}
```
