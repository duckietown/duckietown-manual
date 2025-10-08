```{seo}
:description: The Duckiematrix is a Unity-based photorealistic virtual environment for Duckietown supporting digital twins of Duckietown robots.
:keywords: Duckietown, Duckiematrix, Simulation, digital twin, duckietown simulation, virtual environment, unity, virtual duckiebot, virtual robot
```

(the-duckiematrix-manual)=
# Simulation and the Duckiematrix

```{figure} ../_images/duckiematrix/introduction/duckiematrix-crop.jpg
:name: fig:duckiematrix-crop
:alt: The Duckiematrix is a digital twin virtual simulator for Duckietown

Welcome to the Duckiematrix, where simulation and reality are blurred!
```

The Duckiematrix is a Unity-based virtual environment for Duckietown supporting digital twins of Duckietown robots.

Its purpose is to simulate the physics and aesthetics of a physical Duckietown environment,
as well as the sensing and acting capabilities of Duckietown robots within that environment.

Of course simulation is never exactly like reality, but, from a functionality standpoint, you should be able
to simulate everything that you could do on a real Duckiebot in the Duckiematrix.

It is worth knowing that, at a high level, the Duckiematrix is composed of two main components:

1. The **engine** which performs the simulation the movement (kinematics and dynamics) of the entities in the simulated world
2. The **renderer** which produces the visualization of the environment and is used to simulate the sensors (in particular the camera)

This section includes the basics of how to install and use the Duckiematrix, for more details about how it works
and how you can build on top of it see [the section in the part of this book about developing with the Duckiematrix](advanced-duckiematrix-development)

```{tableofcontents}
```