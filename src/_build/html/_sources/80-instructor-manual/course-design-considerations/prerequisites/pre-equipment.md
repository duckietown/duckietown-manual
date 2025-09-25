```{seo}
:description: Typical infrastructural prerequisites for teaching a Duckietown class (equipment, space, networks, etc.).
:keywords: duckietown, prerequisites, space, equipment, infrastruture, network
```

(prerequisites-space-infra-equip)=
# Space, infrastructure and equipment

Duckietown could be taught completely remotely, or in a traditional "in presence" fashion with frontal presentations only. Nonetheless,

```{attention}
the best part of teaching with Duckietown is the hands-on work that it facilitates.
```

To enable this experience, you will require some items.

(prerequisites-space)=
## Space

Space is an important consideration. You will need a space that is:

* indoors;

* large enough to accommodate an [assembled Duckietown](duckietowns-intro), built in compliance with Duckietown appearance specifications, and the working positions for students operating it;

* reserved for the duration of the class as reconstructing the Duckietown for every lab session will become tedious.

If there is insufficient space for all students in the class to work at the same time, an effective option is to set up a time-sharing system where students have designated preferential time slots.

When building Duckietown inside a room, you want to consider the following factors:

- Must haves:
  - **passive lighting control**: the goal is creating an environment that as much as possible has uniform, diffused, white lighting, as Duckiebots rely on vision for much of their operations. Varying lighting conditions (colored lights, shadows, time-varying illumination, etc.) will create a strong element of disturbance that will translate into frustration among students. Thick curtains near any window help block the variability of lighting from the sun, and normal ceiling lights may be augmented with properly placed additional light sources. Make sure to avoid reflections that may confuse the Duckiebots.

  - A broadband, appropriately set up [internet connection](prerequisites-network);

- Nice to have:

  - **active lighting control**: installing tunable (in color and intensity) LED lights on the room ceiling will allow us to do great things like simulating night/day cycles, enabling many projects;
  - facilities to securely store and safely charge multiple robots at once;
  - coffee and tea machines!

```{tip}
Instruct everyone to remove their shoes before walking on a Duckietown, to prevent leaving dirt marks that will create visual elements of disturbance. Bonus points for wearing Duckiesocks!
```

(prerequisites-infrastructure)=
## Technical Infrastructure and Equipment

Additional equipment is required for things to function properly.

(prerequisites-computers)=
### Computers

To interact with the robots, students will need a computer with a Ubuntu installation. We **strongly** recommend that this is a native installation (as opposed to a virtual machine), as virtual machines can cause weird and hard-to-debug problems when interacting with low-level components like network interfaces.

The recommended version of Ubuntu (as of January 2024) is Ubuntu 22.04. If the student does not already have this installed, then they can choose a dual-boot setup.

- [Mac dual boot instruction](https://help.ubuntu.com/community/MacDualBoot)
- [Windows dual boot instructions](https://help.ubuntu.com/community/WindowsDualBoot)

```{attention}
Every student should have a computer with a native Ubuntu installation:
- **Minimum specifications**: Quad-core at 1.8Ghz, 4GB RAM, 60GB hard drive, GPU compatible with OpenGL 2.1+
- **Recommended specifications**: Quad-core at 2.1Ghz, 8GB RAM, 120GB hard drive, GPU compatible with OpenGL 2.1+
```

Follow the [instructions](setup-sw-intro) to set up the working environment once you have a working Ubuntu installation.

Other operating systems might work, but use them at your own risk. The Duckietown staff is unable to provide support for non-Ubuntu setups, but you can always leverage our community resources to work through your problems if you choose that path.

We are working to provide broader supported compatibility. If you would like additional information on this effort, or to support it, you can reach out to us [on Slack](https://duckietown.com/join-slack).

(prerequisites-network)=
### Network

```{tip}
If working within a corporate network (e.g., in a University), read the following section carefully and prioritize starting a conversation with your IT people. It might be necessary to create a dedicated subnet for your lab to be compliant with typical corporate security guidelines.
```

We like to say in our classes that "**90% of problems in robotics come from networks**", as in all likelihood, this is the thing that is going to cause you the most headaches.

You will need a reliable internet connection for students to:

* Download things (such as Docker images) onto their computer;
* Download things (such as Docker images) onto their robot;
* To communicate with their robot.

The faster the better when it comes to the bandwidth of the connection.

We are going to up and download Gigabytes of data (exercises, activities, agent submissions, etc.) and if many students are all trying to do this at the same time, this could slow things down considerably.

Other than the speed, there are a few other technical requirements for your network:

1. Students will need to be able to [SSH](secure-shell) into their robots, therefore port 22 needs to be open on the router;

2. We make extensive use of the name-discovery tool called [Avahi](https://www.avahi.org/). This is needed so that we do not need to know the IP of the robot to be able to communicate with it. Instead, we can assign a unique name to each robot and then refer to it by name. For example:

    ```
    ping robot_name.local
    ```

3. You can log onto the network with simple credentials (not going through some weird browser authentication).

To do this, Avahi keeps track of all the mappings between the names and the IPs for us. **Some networks do not allow this** - in particular in academic labs, it is very common for network administrators to disable this feature.

As a result, we recommend that you (a) talk to your network administrator and (b) have a dedicated router for the lab that gets its uplink from the university network but that you can directly control. Note that typically this latter option will not be appreciated by your network administrator.

```{tip}
We have compiled [some common problems and solutions](setup-duckiebot-network) that may be helpful. Having some working knowledge of WANs, LANs, Subnets, MAC addresses, DHCP servers, etc., may help along the way.
```
