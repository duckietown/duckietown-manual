```{seo}
:description: The Duckiematrix is a Unity-based photorealistic virtual environment for Duckietown, supporting digital twins of Duckietown robots.
:keywords: Duckietown, Duckiematrix, Simulation, digital twin, duckietown simulation, virtual environment, unity, virtual duckiebot, virtual robot
```

(the-duckiematrix-manual)=
# Simulation and the Duckiematrix

```{figure} ../_images/duckiematrix/introduction/duckiematrix-hero-garage-open.jpg
:name: fig:duckiematrix-crop
:alt: The Duckiematrix is a digital twin virtual environment for Duckietown
:width: 70%

Welcome to the Duckiematrix, where simulation and reality are blurred!
```

The Duckiematrix is a Unity-based virtual environment for Duckietown supporting digital twins of Duckietown robots.

Its purpose is to simulate the physics and aesthetics of a physical Duckietown environment,
as well as the sensing and acting capabilities of Duckietown robots within that environment through [virtual Duckiebots and Duckiedrones](dtmatrix-virtual-duckiebots).

Despite simulation never exactly matching reality, from a functionality standpoint virtual and physical Duckietown robots are equivalent, i.e., you can expect to interact with both in the same way.

## Duckiematrix typical workflow

Before proceeding, it is worth knowing that, at a high level, the Duckiematrix is composed of two main components:

1. The **engine** which performs simulates the movement (kinematics and dynamics) of the entities in the simulated world. You can imagine this as "the world". 
2. The **renderer** which produces the visualization of the world and is used to simulate the sensors (in particular the camera). 

Although not all steps are always necessary, and some can be conflated in unified commands, the typical Duckiematrix workflow is: 

1. **Create the world**: start the **engine** by providing information on the map and entities (e.g., duckiebots, duckiedrones, traffic lights, etc.) that inhabit it;

2. **Observe the world**: start a **renderer** and connect it to the **engine** to "see" the world. Note that (a) there can be multiple (or no) renderers for the same world; (b) the renderer and engine can but do not need to be running on the same computer. 

3. **Attach robots to the world entities**: the entities that inhabit the world at creation are just simulacri, or forms of robots. To give them substance (i.e., an actual agent), *attach* a (or more) robot(s) to an (or more) entity(ies). Note that robots attached to the Duckiematrix can be [virtual](dtmatrix-virtual-duckiebots), or [physical](assembly-instructions-db21j). 

```{seealso}
Additional details can be found [in the developer section of this manual](advanced-duckiematrix-development).
```

```{tableofcontents}
```