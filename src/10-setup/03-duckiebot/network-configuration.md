```{seo}
:description: It is said 90% of problems in robotics stem from networks. Learn how to avoid them by setting your networks up correctly for Duckietown.
:keywords: Duckietown, Duckiebot, network setup, networks
```

(setup-duckiebot-network)=
# Network Configuration in Duckietown

```{needget}
- [An initialized Duckiebot](duckiebot-boot)

- A network router with internet connection

- (optional) An ethernet cable
---
- Learn how to change network configuration on the Duckiebot.

- Basics for debugging network challenges

- A connected Duckiebot
```

Most `dts` commands rely on the connectivity between the Duckiebot, the computer used to interact with it, and the internet.

To make sure all commands work:

- The Duckiebot and computer must appear as physical devices on the same subnet.

- The network must have access to the Internet.

```{warning}
Networks are the most common blocker when using Duckietown. Making sure this step is completely correctly will remove many future headaches.
```

## Wi-Fi connection

Setting up a working Wi-Fi connection between your base station and Duckiebot is a prerequisite for smooth operations.

### Checkpoint

Your network is set up correctly if you can:

```shell
ping DUCKIEBOT_NAME.local
```

while being connected to the internet. You can test this by opening a browser or, for example:

```shell
ping 8.8.8.8
```

````{testexpect}
Run:

```shell
dts fleet discover
```
---
```{figure} ../../_images/setup/handling/fleet_discover.png
:name: fig:fleet-discover-2
:alt: Duckiebot ready on dts fleet discover network discovery tool
:width: 85%

Output of `dts fleet discover` with a connected Duckiebot
```
````

(setup-duckiebot-edit-networks)=
## How to add or edit Wi-Fi networks on a Duckiebot

It is possible to add, remove, or edit networks to which a Duckiebot will connect to by editing the network configuration file, __without__ the need to re-flash the SD card. To do so, one must edit the `/etc/wpa_supplicant.conf` file on the Duckiebot's SD card: [](duckiebot-setup-wifi).

(setup-uni-network)=
### A word on "corporate" networks, e.g., `eduroam`

Some university networks (e.g., the global `eduroam`) have multiple layers of authentication, i.e., a password is not sufficient to access the network. In these cases, the default network configuration settings used by Duckietown are insufficient to connect to the network.

It is possible to edit the `wpa_supplicant.conf` file in your Duckiebot to connect to `eduroam`, but data specific to your university will be required. You will have to coordinate with your network administrator to find out this data.

Here is an [example `wpa_supplicant.conf` setup for the University of Bristol `eduroam`](https://www.wireless.bris.ac.uk/eduroam/instructions/go-wpasup/).

(setup-router)=
## Prerequisites of router and internet connection

Ideally, you work with Duckietown in an environment in which you have administrator powers over the available network. This is the typical case for home networks or, for example, phone hotspots.

In university or corporate networks, for security reasons, some functionalities like local discovery or access to certain ports or websites are made unavailable. Duckietown relies on the following:

- A router that can resolve `DUCKIEBOT_NAME.local` and local IP addresses (that is, local discovery tools such as mDNS).

- Internet access to services such as GitHub, Docker Hub, and Duckietown.

These tools are typically deactivated in corporate networks, such as universities or companies. If this is the case in your working environment, ask your IT team to provide a subnet with Internet access and enabled discovery tools. In the meantime, you could:

- Use a phone with an unlimited data plan as a hotspot.

- Work from your home network.

- Create a temporary "pirate" network by connecting a router at work while your IT team configures the main network settings.

## Ethernet connection between Duckiebot and Base Station

For debugging Wi-Fi connections it might be useful to occasionally connect the computer and Duckiebot through an ethernet connection. The simplest option, when you have physical access to the router, is to connect the Duckiebot via ethernet cable to the router itself. In this way it should immediately appear on the network (e.g., discoverable through `dts fleet discover`).

```{todo}
describe procedure to connect computer directly to Duckiebot via ethernet cable
```

<!--
Direct connections between computer and Duckiebot (...)
-->
