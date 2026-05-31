```{seo}
:description: The supported OS for working with Duckietown is Ubuntu 22.04 or newer. Learn how to install Ubuntu on your computer, and what requirements it should have.
:keywords: computer setup, how to install Ubuntu, duckietown supported OS, why Ubuntu duckietown
```

```{needget}
- A computer (laptop or desktop) satisfying [minimum requirements](setup-computer-requirements)
- A 32GB+ external drive (e.g., the Duckietown SD card + adapter)
---
- A computer with a native Ubuntu installation
```

(setup-computer)=
# Computer setup

The first step in Duckietown is to set up a computer to use as base station.

## Hardware and network requirements

You will need a computer and internet connection to use Duckietown. Find out the requirements here: [](setup-computer-requirements).

## Operating system

Duckietown is designed to introduce learners to the tools and workflows of professional robotics. It is therefore built to work natively with Ubuntu, an open-source distribution of the Linux operating system. 

If this is your first experience with Duckietown, we _strongly recommend_ installing and using **Ubuntu**. 

```{note}
All instructions in this book, unless otherwise explicitly remarked, assume you are using a native Ubuntu installation. Follow the [](setup-install-ubuntu) to find out which Ubuntu version and how to install it on your machine. By native we mean "bare metal", i.e., a dual boot or direct installation, not using a virtual machine.
```

If you are a more experienced user, or absolutely unable or unwilling to install Ubuntu on your computer, we support using **Duckietown Workspaces on macOS and Windows**. Follow [](setup-devcontainer) for installation instructions. 

(setup-why-ubuntu)=
## Why Ubuntu?

At first glance, Ubuntu might be perceived as a barrier to entry to learning AI robotics, especially given the widespread distribution of other operating systems (Windows, macOS) in educational institutions.

We belive that using Ubuntu actually increases accessibility to the science and technology of robot autonomy, for many more reasons than we will list here, but mainly because:

* it is **open source**, **free**, and **available worldwide**
* it is resource-efficient, and runs comparatively well on inexpensive computers
* it is transparent - there is a file for everything
* it has a preexisting large community
* Ubuntu in particular has a UI that is very similar to standard Windows or macOS desktops

If you are concerned about using Ubuntu, it is good. You are here to learn, and progress starts at the edge of our comfort zone.

(setup-install-ubuntu)=
## Installing Ubuntu Desktop

Before installing Ubuntu:

1. Check if your computer will work well with it at [](setup-computer-requirements)
2. Decide if you will install Ubuntu as a dual boot, in which case, ensure you have enough free space to make a partition.

```{tip}
We would recommend that you install Ubuntu as a dual boot when possible. Each time you turn on your computer, you will be able to choose which operating system (OS) to run.
```

```{warning}
The currently supported versions of Ubuntu are 22.04.x and 24.04.x.
```

To install Ubuntu, follow this [Ubuntu Desktop installation tutorial](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).

(setup-win-and-macos)=
## Windows and MacOS supported workflows

It is possible to make Duckietown work with other operating systems, such as Windows or macOS, but it will require extra work in addition to the instructions shown in this manual.

The Duckietown staff is, unfortunately, only able to provide help for the officially supported workflows: (recommended) [native Ubuntu](setup-install-ubuntu), or [Duckietown Workspaces](setup-devcontainer) for Windows or macOS hosts.

Q&As can be found in the [Duckietown archives](setup-account-stack-overflow) and/or in the [Duckietown community on Slack](setup-account-slack).

If you would like to document your solution, we will be glad to review your pull requests. 

(setup-computer-vm-vs-native-ubuntu)=
## A Note on virtual machines

It is possible to run Ubuntu inside a virtual machine (VM) on both Windows and macOS hosts, but given the many possible combinations of VMs, OSs, and architectures, Duckietown staff will not be able to provide support down this path. 

If you are running Ubuntu in a VM (Virtual Machine), **make sure that your computer and Duckiebot appear as physical entities on the same network**. This is achieved by selecting the "bridged network adapter" (e.g., VirtualBox uses NAT by default), which will allow you to be on the same subnetwork as your Duckiebot.

```{note}
When running a VMware machine on a macOS host, it may be necessary to have the following network adapters:
* `Share with my Mac` (for connecting to the Internet).
* `Bridged Networking` (for connecting to your Duckiebot).
```

If using a M-series Mac (ARM architecture), some success has been achieved by emulating a x86 architecture using [UTM](https://mac.getutm.app/).


```{admonition} Reminder
:class: tip
As a reminder: 

- The only supported workflows are: (recommended) [native Ubuntu](setup-install-ubuntu), or [Duckietown Workspaces](setup-devcontainer) for Windows or macOS hosts.

- You can Q&As in the [Duckietown archives](setup-account-stack-overflow) and/or in the [Duckietown community on Slack](setup-account-slack).
```

(setup-computer-requirements)=
## Computer and Internet Requirements for Using Duckietown

Depending on your use case (learner, instructor, developer), you will require a more resourceful machine to meet your Duckietown needs.

### Required (learner):

* 60 GB of hard drive
* Quad-core 1.8GHz
* 4GB RAM
* GPU compatible with OpenGL 2.1+

### Recommended (instructor, developer):

* 150 GB of hard drive
* Quad-core at 2.1Ghz,
* 8GB RAM,
* GPU compatible with OpenGL 2.1+
* [A computer model certified to work with Ubuntu](https://ubuntu.com/certified?q=&category=Laptop&category=Desktop&limit=20)
