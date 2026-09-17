```{seo}
:description: Instructions on how to flash an SD card to initialize a Duckiebot with the fast and easy approach, trading off time for customizability.
:keywords: Duckietown, Duckiebot, flashing, initialization, SD card, Watchtower, dts sd card init, dts sd_card init
```

```{needget}
- An SD card with at least `64 GB` of space

- An SD card adapter appropriate for the computer you are using to flash the SD card

- A broadband internet connection

- 5-15 mins, depending on your internet connection speed

- At least 26 GB of free space on your hard drive before starting
---
- An initialized SD card for your Duckiebot with default configuration settings.
```

(setup-db-sd-card-flashing-fast)=
# The Fast Way

Use this procedure if you want a quicker result, and do not mind having [default settings](db-init-fast-default-settings).

```{tip}
Robots on the same network must have unique names. __Do not follow this procedure if you plan on having multiple Duckiebots on the same network.__
```

```{attention}
By proceeding with these instructions you are accepting the [Duckietown terms of use](initialization-tos).
```

<!--
Internal note: current ente image version 2.0.8
When creating a new image:

1. Use the robot name `entebot` followed by a version number, for example, `entebot208`.

2. Upload the image to the public images bucket in AWS S3.

3. Upload the image to the shared Duckiebot Images Google Drive.

4. Create trackable links with Cuttly.

5. Update redirects in `Cloudflare > duckietown.com > Rules`.

6. Update the robot name in the "default settings" paragraph below.
-->

(initialize-sd-card-video-fast)=
## Duckiebot (`DB21J`) image download

1. Read and understand the [](initialization-tos) before proceeding. For any questions or doubts, [reach out](mailto:info@duckietown.com).

2. Download the Duckietown compressed image:

    - [Download non-customizable `DB21J` Duckiebot `ente` image from AWS](https://duckietown.com/download-duckiebot-ente-sdcard-image-aws).

    - [Download non-customizable `DB21J` Duckiebot `ente` image from Google Drive](https://duckietown.com/download-duckiebot-ente-sdcard-image-googledrive).

    The image is downloaded as a compressed `.zip` file. Programs like Balena Etcher allow flashing this format directly to the SD card. If you are using a different program, unzip the downloaded file to obtain a `.img` file to flash to the SD card.

3. [Install Balena Etcher](https://etcher.balena.io/) or equivalent software.

4. Use Balena Etcher to flash the downloaded image to the SD card.

    Open the Balena Etcher application you just downloaded, and follow the 3 steps instructions (select the file, select the sd card, press start).

5. If Balena Etcher ejected the card, reinsert it, then set a password for the `duckie` account:

    ```shell
    dts sd_card update --type duckiebot --configuration DB21J --password
    ```

    DTS prompts you to enter and confirm the password. It must contain at least eight characters and cannot contain colons or line breaks. The characters you enter are not displayed. The password is applied when the Duckiebot next boots.

6. Configure the network on the Duckiebot:

    This image is pre-configured so that the Duckiebot will connect to a network with SSID `duckietown` and password `quackquack`.

    To have the Duckiebot connect to a different network, you will have to [edit the Wi-Fi settings on your Duckiebot](setup-duckiebot-edit-networks).

    To access the `/etc/wpa_supplicant.conf` file on your Duckiebot, choose one of these options:

    - If you have an Ubuntu computer set up, plug the Duckiebot SD card into your computer using the provided SD card adapter. Navigate to the `/media/duckietown/[...]/etc/` folder, then [edit the Wi-Fi settings](setup-duckiebot-network) with `sudo nano wpa_supplicant.conf`.

    - If you do not have an Ubuntu computer set up, create a temporary hotspot with your phone, Windows, or macOS computer using SSID `duckietown` and WPA-PSK password `quackquack`. Connect the Duckiebot to it after the [first boot](duckiebot-boot), which takes a few minutes. An Internet connection is not required at this stage, so you can disconnect a phone's data plan. From your computer, [SSH into the Duckiebot](handling-how-to-ssh-into-your-duckiebot) and [edit the Wi-Fi settings](setup-duckiebot-network).

    - If you have access to the router and an Ethernet cable, connect your Duckiebot to the router through the Ethernet cable. Connect your computer to the same network, then [SSH into the Duckiebot](handling-how-to-ssh-into-your-duckiebot) to [edit the Wi-Fi settings](setup-duckiebot-network).

7. Plug in the SD card into your Duckiebot (if not already done).

8. Perform the [Duckiebot first boot](duckiebot-boot) sequence (if not already done).

(db-init-fast-default-settings)=
## Default settings

This image has the following default settings:

- Default username: `duckie`.

- No default user password; set one using the `dts sd_card update --password` command above.

- Robot name (hostname): `entebot208`.

- Robot type: `duckiebot`.

- Robot configuration: `DB21J` (works only with the Jetson Nano 4GB developer kit).

- The Duckiebot connects to Wi-Fi named `duckietown` with password `quackquack`.

- Country: `US`.

For additional information on the meaning of these parameters, see: [](setup-db-sd-card-flashing-complete).

(initialization-tos)=
### Legal things - Accepting Duckietown legal terms

By downloading this image you accept the [Duckietown Software License](https://duckietown.com/sw-license/), [Terms and Conditions](https://duckietown.com/terms-and-conditions/) and [Privacy Policy](https://duckietown.com/privacy/), as well as robot configuration-specific licenses due to the presence of third party software in the SD card. Acceptance is mandatory, resistance is futile.

Start by plugging the SD card into your computer using a SD card reader or the USB to microSD card adapter provided in your Duckiebot kit. Make sure the SD card is detected before proceeding.

(sd-card-flashing-troubleshooting-fast)=
## Troubleshooting

```{include} ../../_includes/duckiebot/card-not-written-trouble.md
```

```{include} ../../_includes/duckiebot/card-adapter-write-protection-trouble.md
```

```{include} ../../_includes/duckiebot/card-bad-archive-trouble.md
```

```{include} ../../_includes/duckiebot/card-token-setup-trouble.md
```

Additional information is available at [](db-troubleshooting-network).
