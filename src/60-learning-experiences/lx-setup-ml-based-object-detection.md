(lx-setup-object-detection)=
# LX: Object Detection

```{seo}
:description: Step by step instructions on how to run the object detection learning experience (LX) in Duckietown.
:keywords: Duckietown, Duckiebot, LXs, Learning Experiences, object detection, machine learning, AI, artificial intelligence, deep learning, duckie detector, car obstacle detection, YOLO, YOLO 5, ML, embodied AI, physical AI
```

```{needget}
- Learning experience computer setup: [](duckiebot-lxs)
- A Google account: we will use [Google Colab](https://colab.research.google.com/) and this will require uploading data to [Google Drive](https://drive.google.com/drive/)
- A [Hugging Face](https://huggingface.co) account
- Permission to use the SAM3 autolabeling model: [fill out the request form after having created a Hugging Face account](https://huggingface.co/facebook/sam3)
- (reccomended) A successful Duckiematrix installation: [](the-duckiematrix-first-steps)
- (optional) A "Ready to Go" Duckiebot: [](duckiebot-setup-intro)
---
- Running the Object Detection learning experience.
```

```{attention}
This LX uses online ML tools that require a few extra accounts: for Google and Hugging Face. Links in the box above.

The approval for using the SAM3 model takes a few miuntes, so it's best to do that before starting this LX.
```

This page describes how to run the "Object Detection" learning experience. This learning experience will take you through the process of collecting data, automatically annotating it, and using this to train a neural network to perform object detection using the robot's camera image. We will then use this trained model to ensure that we don't run over any duckie pedestrians in Duckietown. We will use one of the most popular object detection neural networks, called [YOLO (v11)](https://docs.ultralytics.com/models/yolo11/).  You will also have to integrate this trained model into feedback controller so that we don't run over duckies.

```{figure} ../_images/lx-devmanual/lx-object-detection/bbox.png
:alt: duckietown ML object detection LX thumbnail image with annotated duckie
:width: 60%
:name: duckiebot-lx-obj-det-bbox
:align: center

Welcome to the Object Detection LX.  
```

```{admonition} Intended Learning Outcomes
:class: tip
After this learning experience, you will:
- learn about neural networks, and use PyTorch to build one
- collect training data, create a dataset, and annotate it (automatically)
- create, optimize and train your own Duckietown Detector
- fine tune the detector, and test it in simulation and on a physical Duckiebot. 
```

```{warning}
{{ dt_workspace_matrix_lx_warning.format(dt_workspace_note_prefix) }}
```

## About these learning activities

For guided setup instructions, lecture content, and more related to this LX, see [our Self-Driving Cars with Duckietown MOOC on EdX](https://duckietown.com/mooc).

```{note}
This exercise can be run on a virtual Duckiebot in [the Duckiematrix](the-duckiematrix-first-steps), and on a [real Duckiebot](https://get.duckietown.com/products/duckiebot-db21?variant=41543707099311) with off-board agent workflow. On-board agent workflow is work in progress. 
```

(lx-forking-object-detection)=
## Forking the repository

### 1. Create a fork

Navigate to [the LX-Object-Detection repository](https://github.com/duckietown/lx-object-detection).

Find and press the "Fork" button on the top right:

```{figure} /_images/lx-devmanual/intro/duckietown-lx-forking.png
:alt: how to fork a Duckietown LX repository
:width: 90%
:name: duckiebot-lx-forking-object-detection
:align: center

Fork the LX to be able to make local changes while still being able to receive updates.
```

This will create a new repository at: `<your_github_username>/lx-object-detection`.

### 2. Clone the fork

Clone the fork on your computer, replacing your GitHub username in the command below, and navigate to the new folder:

    git clone git@github.com:<your_github_username>/lx-object-detection
    cd lx-object-detection
        
### 3. Configure the upstream repository

Configure the Duckietown version of this repository as the upstream repository to synchronize with your fork.

List the current remote repository for your fork,

    git remote -v

Specify a new remote upstream repository,

    git remote add upstream https://github.com/duckietown/lx-object-detection

Confirm that the new upstream repository was added to the list,

    git remote -v

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every exercise will prompt you to pull from the upstream repository, updating your exercises to the latest version (if available).

(lx-system-update-object-detection)=
## Keeping your System Up To Date

- 💻 These instructions are for `ente` learning experiences. Ensure your Duckietown Shell is set to an `ente` profile (and not a `daffy` one). You can check your current profile with: 
    
    ```
    dts profile list
    ```

    To switch to an ente profile, follow the [Duckietown Manual DTS installation instructions](setup-dts).

- 💻 Pull from the upstream remote to synch your fork with the upstream repo: 

    ```
    git pull upstream ente
    ```

- 💻 Make sure your Duckietown Shell is updated to the latest version: 

    ```
    pipx upgrade duckietown-shell
    ```

- 💻 Update the shell commands: 

    ```
    dts update
    ```

- 💻 Update your laptop/desktop: 

    ```
    dts desktop update
    ```

- 🚙 Update your Duckiebot (even if it is a virtual one): 

    ```
    dts duckiebot update ROBOTNAME
    ``` 
    
    (where `ROBOTNAME` is the name of your Duckiebot - real or virtual.)

(lx-code-editor-lx-object-detection)=
## Launching the Code Editor

```{important}
All `dts code` commands should be executed inside the root directory of the learning experience.
```

Making sure you are inside the path of the specific learning experience you want to work on, open the code editor by running:

```
dts code editor
```

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar
of your browser to access the code editor. The first thing you will see in the code editor are a version of these instructions. At this point you can start following the LX-specific indications shown in your code editor.

(lx-navigating-notebooks-object-detection)=
## Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the
`notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through them in sequence.

In many cases the last notebook will instruct you to write some code inside the
learning experience directory. 

Once you have done that you will need to **build** your code before **testing** it.

(lx-matrix-testing-object-detection)=
### Testing with the Duckiematrix

To test your code in the Duckiematrix you will need a virtual robot attached to an ongoing session.

(lx-create-vbot-object-detection)=
#### 1. Creating and starting virtual Duckiebot

You can create one with the command:

```
dts duckiebot virtual create --type duckiebot --configuration DB21J [VBOT]
```

where `[VBOT]` is the hostname. It can be anything you like, subject to the [same naming constraints of physical Duckiebots](setup-db-sd-card-flashing-complete). Make sure to remember your robot (host)name for later.

Then you can start your virtual robot with the command:

```
dts duckiebot virtual start [VBOT]
```

You should see it with a status `Booting` and finally `Ready` if you look at `dts fleet discover`:

```
     | Hardware |   Type    | Model |  Status  | Hostname 
---  | -------- | --------- | ----- | -------- | ---------
[VBOT] |  virtual | duckiebot | DB21J |  Ready   | [VBOT].local
```

Once you are done for the day, do not forget to stop your virtual robot:

```
dts duckiebot virtual stop [VBOT]
```

If in doubt, you can check the status of your virtual scuderia at any time with:

```
dts duckiebot virtual list
```

(lx-code-matrix-start-object-detection)=
#### 2. Starting the Duckiematrix with the virtual Duckiebot

Now that your virtual robot is ready, you can start the Duckiematrix. From this exercise directory do:

```
dts code start_matrix
```

```{note}
{{ dt_workspace_start_matrix_split_note.format(dt_workspace_note_prefix) }}
```

You should see the Unity-based Duckiematrix simulator start up. For more details about using
the Duckiematrix see [](the-duckiematrix-manual).

```{figure} ../_images/lx-devmanual/lx-object-detection/normal.png
:alt: A step in the Duckietown object detection training process
:width: 70%
:name: duckiebot-lx-obj-det-segmentation
:align: center

Finding duckies.
```

To run the WebGL (browser) version of the Duckiematrix, add the `--browser` flag.

```{note}
For the WebGL (browser) version of the Duckiematrix, if the colors look desaturated, try a different browser.
```

(lx-code-build-object-detection)=
### Building the Code

From inside the learning experience root directory, you can build your code with:

```
dts code build -R ROBOT_NAME
```

where `ROBOT_NAME` can be either a physical or virtual robot. 

(lx-code-test-object-detection)=
### Testing on a Duckiebot or in the Duckiematrix


```{attention}
Before you can test, you will need to:

 - Collect data
 - Annotate that data (automatically)
 - Train your object detection model
 - Export your model
```

🚙 To test your code on your real Duckiebot you can do:

```
dts code workbench -R ROBOT_NAME [--local]
```

```{note}
For the time being, you should include the `--local` flag if `ROBOT_NAME` is a **physical** Duckiebot. This
will cause the code to be run on your laptop which is communicating with your Duckiebot. 
```

💻 To test your code on a virtual robot in the Duckiematrix:

```
dts code workbench -m -R VIRTUAL_ROBOT_NAME
```

(note the `-m` flag which means that we are running in the `matrix`.)


```{figure} ../_images/lx-devmanual/lx-object-detection/train_batch1.jpg
:alt: duckietown object detection learning experience training in batch from real data
:width: 70%
:name: duckiebot-lx-obj-det-training-in-batch
:align: center

Object detector training. 
```

## Troubleshooting

```{trouble}
When running `dts code editor` I get an error: `dts :  No valid DTProject found at '/path/to/lx'`
---
Make sure your are executing the commands from inside a learning experience folder (e.g., `*/lx-object-detection/`)
```

```{trouble}
My virtual robot (named, e.g., `VBOT`) hangs indefinitely when trying to update it.
---
Try to restart it with: `dts duckiebot virtual restart VBOT`
```