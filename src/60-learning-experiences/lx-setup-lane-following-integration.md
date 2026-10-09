```{seo}
:description: Combine the knowledge gained from previous LXs such as modeling, control, computer vision, filtering, etc., into a more complex lane following autonomous behavior.
:keywords: lane following, learning experience, LX, Duckietown, Duckiebot, autonomous driving, self-driving cars, computer vision, dts devel
```

```{needget}
- Learning experience computer setup: [](duckiebot-lxs)
- (recommended) A successful Duckiematrix installation: [](the-duckiematrix-first-steps)
- (optional) A "Ready to Go" Duckiebot: [](duckiebot-setup-intro)
---
- A Duckiebot autonomously following the lane in Duckietown.
```

(lx-setup-lf-integration)=
# 🔥 🆕 LX: Lane Following - Integration

This learning experience is designed to combine the knowledge gained from several of the simpler LXs into one more complex lane following autonomous behavior. 

It also serves as an introduction to the [`dts devel`](https://docs.duckietown.com/ente/duckietown-manual/70-developer-manual/dtproject/creating-demos.html) API which you can use to create new behaviors in Duckietown. 

For guided environment setup instructions, lecture content, and more related to this LX, see [the EdX course page](https://duckietown.com/self-driving-cars-with-duckietown-mooc/).

```{raw} html
<figure style="max-width: 800px; margin: 1.5rem auto;">
  <iframe
    src="https://livid.com/embed/0inEP377lU9-?autoplay=1&amp;loop=1&amp;muted=1"
    title="Lane following - Duckiebot DB21J (no sound)"
    style="display: block; width: 100%; aspect-ratio: 16 / 9; border: 0;"
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture; web-share"
    allowfullscreen
    referrerpolicy="strict-origin-when-cross-origin">
  </iframe>
  <figcaption style="margin-top: 0.5rem; text-align: center;">
    Lane following with a DB21J Duckiebots.
    <a href="https://livid.com/watch/0inEP377lU9-">Watch online</a>
  </figcaption>
</figure>
```

```{admonition} Intended Learning Outcomes
:class: tip

After this learning experience, you will be able to:
- Use the `dts devel` API to deploy your code and create new behaviors in Duckietown.
- Integrate the knowledge gained from previous LXs such as modeling, control, computer vision, filtering, etc., into a more complex lane following autonomous behavior.
- Run and tune the autonomous lane following behavior on a Duckiebot in the Duckiematrix and on a physical Duckiebot.
- Identify common pitfalls, and troubleshoot issues that arise when running the lane following behavior on a Duckiebot in different environments.
```

```{admonition} Available repositories
:class: seealso

- [Learner Repository](https://github.com/duckietown/lx-lane-following) 
- [Recipe/Technical Backend Repository](https://github.com/duckietown/lx-recipe-lane-following)
- 🔒 Instructor Solution Repository: this LX does not require a solutions repository.

To access solution repositories, [become a Duckietown Instructor](https://hub.duckietown.com/plans/?plan=institutional). 
```

{{ dt_workspace_matrix_lx_warning.format(dt_workspace_note_prefix) }}

## About these learning activities

For guided setup instructions, lecture content, and more related to this LX, see [our Self-Driving Cars with Duckietown MOOC on EdX](https://duckietown.com/mooc).

```{include} ../_includes/lx/exercise-offboard-runtime-note.md
```

(lx-forking-lane-following)=
## Forking the repository

### 1. Create a fork

Navigate to [the lx-lane-following repository](https://github.com/duckietown/lx-lane-following).

Find and press the "Fork" button on the top right:

```{figure} /_images/lx-devmanual/intro/duckietown-lx-forking.png
:alt: how to fork a Duckietown LX repository
:width: 90%
:name: duckiebot-lx-lane-following-integration-forking
:align: center

Fork the LX to be able to make local changes while still being able to receive updates.
```

This will create a new repository at: `<your_github_username>/lx-lane-following`.

### 2. Clone the fork

Clone the fork on your computer, replacing your GitHub username in the command below, and navigate to the new folder:

```shell
git clone --recurse-submodules git@github.com:<your_github_username>/lx-lane-following
cd lx-lane-following
```

### 3. Configure the upstream repository

Configure the Duckietown version of this repository as the upstream repository to synchronize with your fork.

List the current remote repository for your fork:

```shell
git remote -v
```

Specify a new remote upstream repository:

```shell
git remote add upstream https://github.com/duckietown/lx-lane-following
```

Confirm that the new upstream repository was added to the list:

```shell
git remote -v
```

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every exercise will prompt you to pull from the upstream repository, updating your exercises to the latest version (if available).

(lx-system-update-lane-following)=
## Keeping your System Up To Date

- 💻 These instructions are for `ente` learning experiences. Ensure your Duckietown Shell is set to an `ente` profile (and not a `daffy` one). You can check your current profile with:

    ```shell
    dts profile list
    ```

    To switch to an ente profile, follow the [Duckietown Manual DTS installation instructions](setup-dts).

- 💻 Pull from the upstream remote to synchronize your fork with the upstream repository:

    ```shell
    git pull upstream ente
    ```

- 💻 Make sure your Duckietown Shell is updated to the latest version:

    ```shell
    pipx upgrade duckietown-shell
    ```

- 💻 Update the shell commands:

    ```shell
    dts update
    ```

- 💻 Update your laptop/desktop:

    ```shell
    dts desktop update
    ```

- 🚙 Update your Duckiebot (even if it is a virtual one):

    ```shell
    dts duckiebot update DUCKIEBOT_NAME
    ```

    (where `DUCKIEBOT_NAME` is the name of your physical or virtual Duckiebot.)

(lx-code-editor-lx-lane-following)=
## Launching the Code Editor

```{include} ../_includes/lx/dts-code-root-important.md
```

Making sure you are inside the path of this learning experience (`cd ./path-to-lxs-in-your-workstation/lx-lane-following`), then open the code editor:

```shell
dts code editor
```

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar of your browser to access the code editor.

The first thing you will see in the code editor is a version of these instructions. At this point you can start following the LX-specific indications shown in your code editor.

(lx-navigating-notebooks-lane-following)=
## Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the `notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through them in sequence. In many cases the last notebook will instruct you to write some code inside the learning experience directory.

Once you have done that you will need to __build__ your code before __testing__ it.

(lx-matrix-testing-lane-following)=
### Testing with the Duckiematrix

To test your code in the Duckiematrix, attach either a physical or virtual robot to a Duckiematrix Entity. The steps below use a virtual robot; for instructions on attaching a physical robot, see [](introduction-duckiematrix-connect-db-to-remote-engine).

(lx-create-vbot-lane-following)=
#### 1. Creating and starting virtual Duckiebot

If you have not done so already (e.g., for a different LX), you can create a virtual Duckiebot with the command:

```shell
dts duckiebot virtual create --type duckiebot --configuration DB21J ROBOT_NAME
```

When you run the command, DTS prompts you to enter and confirm the password for the virtual robot's `duckie` account; the characters you enter are not displayed. `ROBOT_NAME` is the hostname. It can be anything you like, subject to the [same naming constraints of physical Duckiebots](setup-db-sd-card-flashing-complete).

Then you can start your virtual robot with the command:

```shell
dts duckiebot virtual start ROBOT_NAME
```

You should see it with a status `Booting` and finally `Ready` if you look at `dts fleet discover`:

```text
     | Hardware |   Type    | Model |  Status  | Hostname 
---  | -------- | --------- | ----- | -------- | ---------
ROBOT_NAME |  virtual | duckiebot | DB21J |  Ready   | ROBOT_NAME.local
```

Once you are done for the day, do not forget to stop your virtual robot:

```shell
dts duckiebot virtual stop ROBOT_NAME
```

If in doubt if any of your virtual Duckiebots in running or not, you can check the status of your virtual scuderia at any time with:

```shell
dts duckiebot virtual list
```

(lx-code-matrix-start-lane-following)=
#### 2. Starting the Duckiematrix with the virtual Duckiebot

Now that your virtual robot is ready, you can start the Duckiematrix. From this LX directory:

```shell
dts code start_matrix [--no-renderer] [--browser]
```

{{ dt_workspace_start_matrix_split_note.format(dt_workspace_note_prefix) }}

To run the WebGL (browser) version of the Duckiematrix, add the `--browser` flag.

```{include} ../_includes/duckiematrix/webgl-browser-note.md
```

You will see the Unity-based Duckiematrix simulator start up. 

From here you can click anywhere on the window and click <kbd>ENTER</kbd> to make it become active, and then move the duckie towards the Duckiebot with the <kbd>w</kbd>, <kbd>a</kbd>, <kbd>s</kbd>, and <kbd>d</kbd> keys, and you can move the camera angle to view the Duckiebot with the mouse. If you are close enough to your Duckiebot, you can board it with the <kbd>E</kbd> key, and drive the Duckiebot around with <kbd>w</kbd>, <kbd>a</kbd>, <kbd>s</kbd>, and <kbd>d</kbd> keys. 

If you get very lost from the road and you want to come back, you can do so with the <kbd>R</kbd> key.

```{include} ../_includes/lx/reset-duckiebot-position-note.md
```

(lx-code-build-lane-following)=
### Building the Code

Part of the learning activities in this LX require to write the code that composes the various functions of the lane following behavior. Once you have written your code, you will need to build it before testing it using the `dts devel build -H ROBOT_NAME` command. 

The `dts devel` workflow is more advanced (and powerful) than the `dts code` commands that we typically use in LXs. For details, refer to the last notebook of this LX.

(lx-code-test-lane-following)=
### Testing on a Duckiebot or in the Duckiematrix

🚙 To test the code of this LX on your Duckiebot - whether physical or virtual - use the `dts devel` workflow. Details are provided in the pertinent notebook, accessible with `dts code editor`. 

## Troubleshooting

```{include} ../_includes/lx/ekf-code-editor-no-project-trouble.md
```

```{include} ../_includes/lx/virtual-robot-update-trouble.md
```
