{vscode-dev-on-db}
# VS Code: Attach to a Duckiebot

```{seo}
:description: How to attach Visual Studio Code to a Duckiebot container for faster development.
:keywords: Duckietown, Duckiebot, VS Code, Docker, development
```

This guide shows how to attach Visual Studio Code to a running container on your Duckiebot using the Container Tools extension. This lets you edit code and use the VS Code UI directly inside the robot’s container.

```{vimeo} 1118803369
:alt: Attaching VS Code to a Duckiebot container

Short video walkthrough of attaching Visual Studio Code to a running Duckiebot container using the Docker extension.
```

```{needget}
* VS Code with the [Container Tools extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-containers) installed
* Network access to the Duckiebot.

---
* An IDE (VSCode) connected to the running devcontainer on the Duckiebot.
```

## Add the Docker Context

1) Create a Docker context that points to your Duckiebot over TCP on port 2375:

```shell
docker context create ROBOT_NAME --docker "host=tcp://ROBOT_NAME.local:2375"
```

2) In VS Code, select this context in the Docker view (next section shows how).

## Navigate to the Target Container

3) Open the Docker view from the Activity Bar.

```{figure} ../../../_images/developer/vscode-development-on-duckiebot/step-1.png
Click the Docker icon in the Activity Bar to open the Docker view.
```

4) Expand “Docker Contexts” at the bottom of the panel.

```{figure} ../../../_images/developer/vscode-development-on-duckiebot/step-2.png
Expand the Docker Contexts section in the Docker view.
```

5) Select the context that corresponds to your Duckiebot (e.g., `ROBOT_NAME`).

```{figure} ../../../_images/developer/vscode-development-on-duckiebot/step-3.png
Choose the Duckiebot context so its containers are listed above.
```

6) Verify the containers list shows your Duckiebot’s containers.

```{figure} ../../../_images/developer/vscode-development-on-duckiebot/step-4.png
The containers tree should populate for the selected Duckiebot context.
```

## Attach Visual Studio Code

7) Locate the target container (e.g., `dts-run-dt-core`). Scroll if needed.

```{figure} ../../..//_images/developer/vscode-development-on-duckiebot/step-5.png
Scroll through the containers list to locate the target container.
```

```{figure} ../../../_images/developer/vscode-development-on-duckiebot/step-6.png
Focus the container entry so its context actions are available.
```

8) Right‑click the container and choose “Attach Visual Studio Code”.

```{figure} ../../../_images/developer/vscode-development-on-duckiebot/step-7.png
Open the container’s context menu and select “Attach Visual Studio Code”.
```

## Start editing on the Duckiebot

9) A new window opens inside the container. Open your project folder and start editing, running terminals, or using extensions as needed.

```{figure} ../../../_images/developer/vscode-development-on-duckiebot/step-8.png
The new VS Code window is attached to the container.
```

10) Use the integrated terminal inside this window for container-scoped commands.

```{figure} ../../../_images/developer/vscode-development-on-duckiebot/step-9.png
Use terminals and extensions as usual, now running inside the container.
```

## Tips

- **Terminals:** Use the integrated terminal for commands that must run inside the container.
- **ROS tools:** If the container has ROS installed and is connected to the robot’s ROS network, tools like `rostopic` work from the terminal.
- **Persisting changes:** Changes inside a container are automatically synced to your laptop using [mutagen](https://mutagen.io/).

## Troubleshooting

```{trouble}
Cannot see Duckiebot containers in VS Code.
---
Ensure the Docker context is set to the Duckiebot and that containers are running. Switch context from the status bar in the Container tab.
```

```{trouble}
Attach Visual Studio Code is missing from the menu.
---
Install/update the VS Code Container Tools extension and right‑click directly on a running container.
```
