```{seo}
:description: Explore the Duckietown LX Editor Interface and understand how learners interact with notebooks and solution code.
:keywords: Duckietown, LX editor, learning experience, robotics education, notebooks
```

(dts-code-editor)=
# `dts code editor`

## What does it do?

The `dts code editor` command provides a local code editor that you will use to work through learning 
experience notebooks and develop agents to run on your Duckiebot - right in your browser.

## How do I run it?

Open the code editor by running the following command

```
dts code editor
```

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar
of your browser to access the `VSCode` powered code editor. 

```{note}
If your Operating System supports it, the page should be opened automatically for you in a new browser
tab as soon as it is ready to be opened.
```

```{figure} ../_images/lx-devmanual/consume/editor-url.png
:name: editor_url_1
:alt: Url to access your VSCode editor in the browser.
:align: center
:width: 90%

Url to access your VSCode editor in the browser.
```

The first thing you will see is the README document, which should contain the learning objectives for the LX.

```{figure} ../_images/lx-devmanual/consume/code-editor.png
:name: code_editor_2
:alt: The Duckietown VSCode Learning Experience editor.
:align: center
:width: 90%

The VSCode Learning Experience editor.
```

Once you have read about the learning experience goals in the README document, you can open the `notebooks` directory using the file navigation on the left side of the editor. The activities in the `notebooks` directory contain the main guidance and content of a learning experience. 

```{figure} ../_images/lx-devmanual/intro/hello-world-notebook.png
:name: hello_world_notebook_3
:alt: Duckietown hello world learning experience
:align: center
:width: 90%

The first Hello World notebook will guide you through editing and running the activity.
```

Follow the instructions to complete each notebook in sequence.  If you are working through the **hello-world** LX, complete the following notebooks to create an image filter and explore the editor features:

* 01-Notebook-Activities
* 02-Code-Activities

Then return to this page and continue on to the `dts workbench` command.

```{hint}

Strengthen your test-driven development (TDD) habits by using the Testing interface in the `VSCode` 
editor to run the provided unit tests for each function you complete in an LX. 
This will confirm that your solution performs as expected before you run it in simulation or 
on your Duckiebot. Note that the beaker symbol to open the Testing interface may not appear in the sidebar 
until after you've opened one of the Python files in the `packages` directory.

``{figure} ../../_images/lx-devmanual/consume/test-interface.png
:name: test_interface_4
:alt: Duckietown LX example test interface
:align: center
:width: 90%
``

```


## Troubleshooting

If you run into any issues using this command, you can search the troubleshooting symptoms below or 
reference the [](how-to-get-help) section of this manual.

```{trouble}

`dts :  The path '/home/myuser/not_an_lx_directory' does not appear to be a Duckietown project. 
     :  The metadata file '.dtproject' is missing.`

---
You need to be in the root directory of the LX in order to run the `dts code` commands.
```

## What's Next?

Once you've completed the first two notebooks in the **hello-world** learning experience, continue on to the next page to use the workbench tools and drive a Duckiebot in the Duckietown simulator.

## Extra Options

```{warning}
If this is your first time using the `dts code` workflow, do not worry about the following section just yet. 
Continue on to the next page to run your first LX activity.
```

Once you are comfortable with the `dts code` workflow, you may want to use some additional control provided 
over each command. This section documents each of the flags available to extend the `dts code editor` command.

You can also explore the [Behind the Scenes - dts code editor](behind-the-scenes-code-editor) chapter 
for more details on what happens in the background when you run the `dts code editor` command.

### Command options

```
usage: dts [-h] [-C WORKDIR] [-u USERNAME] [--distro DISTRO] [--bind BIND] [--no-build] [--build-only] [--recipe RECIPE] [--image IMAGE] [--plain] [--no-pull] [--keep] [--impersonate IMPERSONATE] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -C WORKDIR, --workdir WORKDIR
                        Directory containing the project to open the editor on
  -u USERNAME, --username USERNAME
                        The docker registry username to use
  --distro DISTRO       Custom distribution to use VSCode from
  --bind BIND           Address to bind to
  --no-build            Whether to skip building VSCode for this project, reuse last build instead
  --build-only          Whether to build VSCode for this project without running it
  --recipe RECIPE       Path to a custom recipe to use
  --image IMAGE         Docker image to use as editor (advanced use only)
  --plain               Whether to skip building VSCode for this project, use plain VSCode instead
  --no-pull             Whether to skip updating the base VSCode image from the registry
  --keep                Whether to keep the VSCode once done (useful for debugging)
  --impersonate IMPERSONATE
                        Username or UID of the user to impersonate inside VSCode
  -v, --verbose         Be verbose
```