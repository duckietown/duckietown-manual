```{seo}
:description: Example student projects and project ideas in Duckietown.
:keywords: Duckietown, projects, student projects, project ideas
```

(student-project-ideas)=
# Student Project Ideas

Depending on what topics you are covering as components of your class, possible project ideas may differ. 

In general, projects can aim to improve on an existing capability within Duckietown, or add something new. If choosing to add something new, it could be a single component that exists within the larger structure that we have defined, or it could replace everything with some totally different approach (e.g., to use end-to-end machine learning). 

```{note}
We keep a non-exhaustive collection of [videos of past student projects on Vimeo](https://vimeo.com/showcase/9972073). If you would like us to add your project to the list, [reach out to us](mailto:info@duckietown.com)!   
```

(student-projects-improving)=
## Improving Existing Components

A sound strategy for coming up with potential projects is to build upon existing behaviors. The main code repository that contains the algorithmic components that run on the Duckiebot is the [dt-core](https://github.com/duckietown/dt-core) (see [](code) for details on the code structure in Duckietown). Within it are packages that are part of the core [lane following](duckiebot-demo-lf), or more advanced indefinite navigation, demos. 

The core components of lane following include:

* [Color correction with the "anti-Instagram" package](https://github.com/duckietown/dt-core/tree/ente/packages/anti_instagram)
* [Line detection](https://github.com/duckietown/dt-core/tree/ente/packages/line_detector)
* [Projection of line segments to the ground plane](https://github.com/duckietown/dt-core/tree/ente/packages/ground_projection)
* [Fusion of the line segments with a histogram filter](https://github.com/duckietown/dt-core/tree/ente/packages/lane_filter)
* [Feedback control to drive down the lane](https://github.com/duckietown/dt-core/tree/ente/packages/lane_control)
* [A simple finite-state machine](https://github.com/duckietown/dt-core/tree/ente/packages/fsm)

These implementations are meant to be for reference, and there certainly are other ways of implementing each of these blocks. A possible way to structure a project could be to replace or improve on one of these core components and then see the effect on the overall performance of the lane following behavior. 

Additional components that contribute to the indefinite navigation (where a Duckiebot drives indefinitely in a city with intersections and traffic lights) include:

* [Detection of fiducial markers called "Apriltags"](https://github.com/duckietown/dt-core/tree/ente/packages/apriltag)
* [Detection of flashing LEDs for intersection coordination](https://github.com/duckietown/dt-core/tree/ente/packages/led_detection) 
* [Detection of the red stop line](https://github.com/duckietown/dt-core/tree/ente/packages/stop_line_filter)
* [Traversing intersections](https://github.com/duckietown/dt-core/tree/ente/packages/unicorn_intersection)
* [Coordination at intersections](https://github.com/duckietown/dt-core/tree/ente/packages/explicit_coordinator)
* [A more complex configuration of the finite state machine](https://github.com/duckietown/dt-core/blob/ente/packages/fsm/config/fsm_node/indefinite_navigation.yaml)

These represent a possible implementation of this indefinite navigation behavior but, as above, there could be improvements. 

Projects of this type are possibly slightly more ambitious projects as these packages are less well-tested, and students should be more prepared to have to work independently to make things work well. 

```{tip}
One idea could be to structure the entire suite of projects as having the objective to get one more complex behavior such as indefinite navigation to work. 
```

Finally, other packages exist in the repository that worked at some point but probably haven't been tested in a while, such as:

* [Vehicle detection](https://github.com/duckietown/dt-core/tree/ente/packages/vehicle_detection)
* [Dead Reckoning](https://github.com/duckietown/dt-core/tree/ente/packages/deadreckoning)

These may serve as starting points or inspiration, but the students will in all likelihood have to do significant testing or develop their replacement. 

(student-projects-hierarchy)=
## Hierarchy of potential autonomous behaviors

We note that a neat hierarchy of autonomous behaviors may be envisioned for Duckiebots driving in Duckietowns. 

We briefly describe each behavior as source of potential inspiration for additional student projects. This is not a comprehensive list, as other behaviors may be conceived that don't even require city environments. 

```{figure} ../../../_images/instructor-manual/auto-behaviors-hierarchy.png
:name: other autonomous behaviors
:scale: 40%
:align: center

Autonomous behaviors can build on each other in terms of complexity.
```

```{list-table}
:header-rows: 1
:name: mooc-exercises-table
* - BEHAVIOR NAME
  - DESCRIPTION
  - CITY CONFIGURATION
* - Lane Following (`LF`)
  - A single Duckiebot drives indefinitely in a Duckietown without intersections.
  - City loop (without intersections).
* - `LF` with intersections and no traffic lights (`LF-I_noTL`)
  - A single Duckiebot drives indefinitely in a Duckietown with intersections. No intersection is equipped with traffic lights. The additional challenge here is introducing a finite state machine, having Duckiebots stop at intersections, read traffic signs, and navigate intersections before switching back to lane following mode.
  - City with intersections but no traffic lights.
* - `LF` with vehicles on opposite lanes (`LF-V_O`)
  - Same as `LF`, but with two Duckiebots on the map starting in opposite lanes. The additional challenge with respect to `LF` is to be robust to sensory perturbations caused by the lights of the vehicle on the opposite lane. Moreover, Duckiebots must at all times stay in their lane (strictly) to ensure success. 
  - City loop (without intersections).
* - `LF` with intersections (`LF-I`)
  - A single Duckiebot drives indefinitely in a Duckietown with intersections, which may or may not be equipped with traffic lights. The additional challenge here is centralized coordination (LED detection and interpretation).
  - City with intersections (with or without traffic lights).
* - `LF` with pedestrians (`LF-P`)
  - A single Duckiebot navigates a city without intersections, detecting and avoiding (when possible) "pedestrians" (i.e., duckies). The challenge here is detecting objects, and planning around them.
  - City loop (without intersections), but with duckies in the road.
* - `LF` with other vehicles (`LF-V`)
  - Multiple Duckiebots drive indefinitely in a city without intersections. Duckiebots are allowed to be in the same lane. The challenge here is traffic management, i.e., detecting other Duckiebots and maintaining a safe distance from them.
  - City loop (without intersections, without duckies).
* - `LF` with intersections and pedestrians (`LF-IP`)
  - This challenge is similar to `LF-I`, with the additional complication of potentially having pedestrian inside intersection tiles. 
  - City with intersections (with or without traffic lights), and duckies on the road.
* - `LF` with pedestrians and other vehicles (`LF-PV`)
  - The union of `LF-P` and `LF-V`. Duckiebots must be able to detect and avoid both static and moving obstacles (duckies and Duckiebots, respectively).
  - City loop (without intersections), with duckies on the road.
* - `LF` with intersections and other vehicles (`LF-IV`)
  - Multiple Duckiebots navigate indefinitely in a city with intersection, equipped or not with traffic lights. The additional challenge here is dealing with decentralized coordination - i.e., introducing a protocol for having Duckiebots negatiate safe crossing of intersections.
  - City with intersections (with or without traffic lights), and other vehicles on the same or opposite lanes.          
* - `LF` with intersections, pedestrians, and other vehicles (`LF-IPV`)
  - This is the ultimate challenge, where any number of Duckiebots can navigate indefinitely in any city configuration, with pedestrians. 
  - All configurations allowed (with intersections, duckies on the road, and multiple vehicles in any lane).  
```

(student-projects-end2end)=
## New End-to-End Behaviors

Another different project idea is to replace all the autonomy stack in [dt-core](https://github.com/duckietown/dt-core/tree/ente/) with an entirely different approach. To this end, the 

[templates](https://github.com/duckietown/docs-AIDO/tree/daffy/book/AIDO/30_task_embodied)

<!-- removing links to old-docs as server is temporarily down. Restore once server is back up or relevant sections moved elsewhere.
[templates](https://docs-old.duckietown.org/daffy/AIDO/out/embodied.html)
-->

and 

[baselines](https://github.com/duckietown/docs-AIDO/tree/daffy/book/AIDO/31_task_embodied_strategies)

<!-- removing links to old-docs as server is temporarily down. Restore once server is back up or relevant sections moved elsewhere.
[baselines](https://docs-old.duckietown.org/daffy/AIDO/out/embodied_strategies.html) 
-->

that were developed for the [AI Driving Olympics](https://duckietown.com/research/ai-driving-olympics/) may prove useful or at least a source of inspiration (although they may need some updating).

```{note}
Even more advanced behaviors end up becoming published research. You can find some examples as source of inspiration on the [research papers page of our website](https://duckietown.com/research-papers/).
```