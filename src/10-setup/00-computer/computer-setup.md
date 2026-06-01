```{seo}
:description: Duckietown supports workflows on Ubuntu (22+), macOS and Windows. Learn about computer and network requirements for enjoying Duckietown.
:keywords: duckietown minimum requirements, supported OS, duckietown supported OS
```

```{needget}
- A computer (laptop, or desktop)
---
- Knowledge of best approach to installing Duckietown on your computer
```

(setup-computer)=
# Computer setup

The first step in Duckietown is to set up a computer to use as base station.

## Hardware and network requirements

You will need a computer and internet connection to use Duckietown. Find out the requirements here: [](setup-computer-requirements).

## Operating system

Duckietown is designed to introduce learners to the tools and workflows of professional robotics. It is therefore built to work natively with Ubuntu, an open-source distribution of the Linux operating system. 

If this is your first experience with Duckietown we _strongly recommend_ installing, either as dual boot or standalone installation, and using **Ubuntu** by following these instructions: [](setup-install-ubuntu). 

If you are a more experienced user, we support **Duckietown Workspaces on macOS and Windows**. Follow [](setup-devcontainer) for installation instructions. 

```{note}
For the rest of the book, follow the "Ubuntu" and "Duckietown Workspaces" tabs depending on your setup. If tabs are not specified for a set of instructions, those can/should be run in both environments.  
```

(setup-computer-vm-vs-native-ubuntu)=
## A note on virtual machines

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
