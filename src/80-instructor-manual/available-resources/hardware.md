```{seo}
:description: Duckietown robots include self-driving cars (Duckiebots), autonomous quadcopters (Duckiedrones) and a modular smart-city environment (Duckietown). 
:keywords: Duckietown, Duckiebot, Duckiedrone, hardware, robot
```
(hardware)=
# Duckietown Hardware

We are firm believers that you can't learn about robotics without a robot. 

Our core objective in the design of the hardware was to provide a platform that is as simple and inexpensive as possible, but still able to provide a wide range of challenging and reproducible learning experiences. 

```{seealso}
To acquire Duckietown hardware, visit the [Duckietown online store](https://get.duckietown.com/).
```

(duckiebots-hardware)=
## Duckiebots

The Duckiebot is a small differentiable drive robot that is simple yet powerful. It is equipped with a camera, wheel encoders, as well as other sensors. It is powered by a [custom battery](db-opmanual-dtbattery-v2) that we have built to enable live diagnostics and advanced power management behaviors. The `DB21` family of Duckiebots use [NVIDIA Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit) for computation.

```{figure} ../../_images/instructor-manual/db21m.jpeg
:name: duckiebot
:scale: 60%
:align: center

The Duckiebot is a small-scale robot that we have developed for autonomy education and research. 
```

The platform has gone through several iterations, for a full breakdown of the configurations see [](duckiebot-configurations). 

Also, for complete detail about the components of the Duckiebot, as well as its operation, refer to the Part 1 of this book.

(duckietown-hardware)=
## Duckietown

To guarantee the reliable performance of the Duckiebot, we have also designed a custom environment, the Duckietown, for the Duckiebot to operate in. 

```{figure} ../../_images/instructor-manual/duckietown.webp
:name: duckietown
:scale: 40%
:align: center

Duckiebots operate in Duckietowns, which can have aribitrary topologies as long as the appearance specifications are respected.
```

The environment is very tightly specified. For full details, visit the [Duckietown Operation Manual](duckietowns-intro). 

You might be tempted to build a Duckietown out of off-the-shelf components. While it is totally possible, make sure to understand the underlying design criteria to prevent future headaches. 

(drones-hardware)=
## Duckiedrones

We have also more recently developed a flying robot, that we refer to as the Duckiedrone. 

Duckiedrones are Raspberry Pi-powered autonomous quadcopters, and are designed to introduce younger learners to robotics and autonomy. 

For full details on the platform, visit the [Duckiedrone Operation Manual](duckiedrone-redirect). 

```{figure} ../../_images/instructor-manual/duckiedrone.webp
:name: duckiedrone
:scale: 60%
:align: center
:alt: The Duckiedrone is a Raspberry-Pi based autonomous quadcopter.

The Duckiedrone is a Raspberry-Pi based autonomous quadcopter.
```


<!--
Add this back once Duckiedrone stuff intetgrated into this book
Course materials based on the Duckiedrone have been developed largely by [Prof. Stefanie Tellex](https://scholar.google.com/citations?user=Pd8-ju0AAAAJ&hl=en) and her team at Brown University. 

For details, check out the [Introduction to Robotics with Drones](book-course-intro-to-drones:book-intro-drones-duckiesky-tellex-brown) book in the library. 
-->