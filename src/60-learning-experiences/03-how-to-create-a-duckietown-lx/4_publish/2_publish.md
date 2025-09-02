```{seo}
:description: Learn how to publish your Duckietown Learning Experience (LX) project using the `dts code publish` command, and manage repositories and branches effectively.
:keywords: Duckietown, Learning Experience, LX, publish, dts code, GitHub, version control, repository management
```

(how-to-publish-lx)=
# Publishing Your LX

The three directories making up an LX can be published to their respective repositories using the `dts code publish` command.  

This provides a streamlined interface for managing repositories and branches so that your LX directories will never be out of sync with each other across the development project.

## LX publishing requirements

The following information is needed to publish an LX: 

```{list-table} LX publishing requirements
:header-rows: 1
:name: publish-table

* - Information
  - Description
* - Repository / Branch for each LX portion
  - Each of the three LX directories (`lx`, `recipe`, `solution`), should be published to a different repo. Students 
  should have access to the LX and optionally the solution, but the recipe should remain private to avoid 
  complicating the `dts code` learner workflow. 
* - Version
  - The version description will be used as the commit message when you publish to a set of GitHub repositories.
```

## Publishing an LX development project

Publish your LX development project by entering the main project directory (one level above the `lx`, `recipe`, and 
`solution` directories, **not** within them) and running

    dts lx publish

Wait for the form UI to appear or click on the URL provided in the terminal to access the following form:

```{figure} ../../_images/lx-devmanual/create/publish-interface.png
:name: publish-interface

The LX publish tool configuration interface.
```

Then fill in the required information.  First, the repository and branch for each of the three LX portions:

```{figure} ../../_images/lx-devmanual/create/publish-repo.png
:name: publish-repo

The repository and branch that each directory will be published to.
```

```{important}
Each of the three LX directories (`lx`, `recipe`, `solution`), should be published to a different repo. Students 
  should have access to the LX and optionally the solution, but the recipe should remain private to avoid 
  complicating the `dts code` learner workflow.
```

The information you enter will automatically save, so that you can conveniently publish frequently. You may update 
these values during any future publish as the form will appear every time.

```{figure} ../../_images/lx-devmanual/create/publish-default.png
:name: publish-default

The default values will be saved for convenient iterative publishing.
```

The version description you provide will be used as the commit message when pushing to the repositories.

```{figure} ../../_images/lx-devmanual/create/publish-version.png
:name: publish-version

The publish commit message.
```

Select `Publish` and return to the terminal to confirm that your artifacts were pushed successfully.
