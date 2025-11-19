```{seo}
:description: Comprehensive guide to using Git and GitHub within the Duckietown modular software ecosystem, covering branches, commits, pull requests, and best practices.
:keywords: Git, GitHub, version control, Duckietown, branches, commits, pull requests, software modularity, development workflow
```

(sec:developer_basics_git)=
# Git

Every time there is a large project, with many contributors and the need for code versioning and history, developers rely on VCS (Version Control Systems) tools.

Duckietown uses **Git** as VCS and [GitHub](https://github.com) as a service provider for it. The Duckietown organization page on GitHub is [github.com/duckietown](http://github.com/duckietown).


## Monolithicity versus Modularity

Whether a software project should be monolithic or modular is
one of the most debated decisions that a group of developers
faces at the beginning of a software project. Books have been
written about it. Duckietown started as a monolithic project,
and some of us still remember the infamous
[Software](http://github.com/duckietown/Software) repository,
and only later transitioned to a full modular approach.

Duckietown distinguishes between **modules** and **nodes**:

* A **module** is a high-level package (for example, _autonomous-driving_).

* A **node** is the smallest software entity, usually responsible for one task (for example, _traffic-sign-detection_). Nodes always reside inside modules.

Each module has its own repository under the Duckietown GitHub organization. Personal or course-specific modules can live in separate GitHub accounts while remaining fully compatible with the ecosystem.

```{tip}
Be brave, Duckietown has hundreds of repositories.
```
(dev-basics-git-terminology)=
## Git

The most frequently used Git concepts are summarised below.

### **Repository**

A repository (or _repo_) holds the complete file set for a project plus the entire revision history, i.e., the history of every change done on each file.


### **Branch**

Branches constitute threads of changes within a repository. Though we
call them branches, do not try to force an analogy with tree
branches, they are similar in spirit but quite different in how
they work.

A repository is not allowed to exist without a branch, and
every operation inside a repository only makes sense in the context
of a branch (the _active_ branch).
A repository can have many branches, but only one active at the time.

Every Git project has at least one main branch, usually called
the `master` or `main` branch.

Branches are used in different scenarios, allowing different developers to work simultaneously on their own task without having their work affect or be affected by the others.

For example, after a project is released with version `1.0.0`, one team might be tasked to develop a new feature for the version `1.1.0` milestone, while another team is asked to fix a user-reported bug which be patched in a version `1.0.1`.

Branch operations, like switching between branches or checking which is the active branch, are performed through the command `git branch`.

### **Commit**

A commit is an atomic set of changes recorded in the repository history and is identified by a unique `SHA-1` hash.

When you create/delete/edit one or more files in a repository,
and you are confident enough about those changes, you can commit (or, "save" them to the online version system) them to the branch using the workflow:
* `git add <file(s)>`, e.g., `git add .` to indicate all changes
* `git commit -m "Replace me with some informative message regarding the commit."`.

```{note}
A commit is not a snapshot (or a copy) of the entire repository
at a given point in time. Each commit contains only the incremental
difference from the previous commit, called *delta* in Git.
```

A chain of commits in which all the ancestors are included makes a
branch. Since every commit is linked to its parent, a branch is
simply a *pointer* to a commit (the full chain of commits can always
be reconstructed from the commit).
In other words, you can think of branches as human friendly labels
for commits. Every time you create a new commit, the pointer of the
current branch advances to the newly created commit.


### **Tag**

A tag is a human friendly name for a commit but unlike branches, tags
are read-only. Once created, they cannot be modified to point to
a different commit.

Tags are commonly used for labeling commits that constitute
milestones in the project development timeline, for example a release.


### **Fork**

A fork is basically a copy of someone else's repository.
Usually, you cannot create branches or change code in other
people's repositories, that is why you create your own copy of it.
This is called `forking` and allows you to experiment without affecting the original.


### **Remote**

A git *remote* is a copy of your repository hosted by a Git service
provider, e.g. [GitHub](https://github.com). Remotes allow you to
share (`push`) your commits and branches so that other developers can `fetch`
them. Remotes are the same as local repositories, but they are reachable
over the internet.

You can use the commands `git fetch` and `git push` to bring your
local copy of the repository in sync with a remote, by downloading
commits or uploading new commits respectively.


### **Merging branches**

Merging integrates the history of one branch into another. Conflicts occur when the same lines of code differ between branches and must be resolved manually.

Imagine having branched out from `master` to `new-patch` to deploy a new bug fix. Now you want to incorporate these changes back in the `master` branch, which hosts your main code. The **merge** operation does exactly that. It takes the changes done in `new-patch` and applies them
to `master`.

Often Git will manage to apply these changes seamlessly. However,
if both `new-patch` and `master` have changes to the same line of code, Git
will not be able to determine automatically which of the two changes should be preserved. These are called _merge conflict_ and will have to be solved manually, by selecting which of the two version to keep.

### **Pull Requests**

A pull request (or, **PR**) on GitHub proposes that changes from one branch (often in a fork) be merged into another branch and provides a discussion and review interface before the merge is executed.

A pull request can be seen as a three-step merge operation between two
branches where the changes are first _proposed_, then _discussed and adapted_
(if requested), and finally _merged_.

PRs are a better practice than direct merging, as it provides an extra-layer of revision before potentially compromising the main code with undesirable changes.

## Common operations

### **Fork a repository on GitHub**

To fork a repo you have to go to the repository's webpage and click
on the fork button in the upper right corner.


### **Clone a repository**

Cloning a repository is the act of creating a local copy of a remote
repository. A repo is cloned only at the very beginning, when you
still do not have a local copy of it.

To clone a repository, either copy the HTTPS or SSH URL given on
the repository's webpage, then:

    git clone [REPOSITORY-URL]

This will create a directory in the current working path with
the same name of the repository and the entire history of commits
will be downloaded onto your computer.


### **Create a new branch**

The command for creating a new branch is a little bit
counter-intuitive, but you will get use to it:

    git checkout -b [NEW-BRANCH-NAME]

This creates a new branch pointing at the same commit your
currently active branch is pointing at. In other words, you will
end up with two branches pointing at the same commit. Note that
after you issue this command, the newly created branch becomes
your active branch.

### **Inspecting working tree status**

In Git, the term *working tree* indicates all the changes
that are not committed yet. You can think of it as your workspace.
When you create a new commit, the hash for the current working tree
is computed and assigned to the new commit together with the changes
since the last commit. The working tree clears as you commit changes.

```{note}
You cannot create commits from a clean working tree.
```

Use the command `git status` to inspect the status of your working
tree.


### **Create a new commit**

A commit is created through a two-step process. First, mark all the
changes that will be part of the new commit:

    git add <file(s)>

```{tip}
The command `git status` will always show you which changes are
marked to be used for a new commit and which changes are not.
```
Second, create the actual commit:

    git commit -m "Replace me with a really informative message."

to create a new commit. Replace `[COMMIT-MESSAGE]` with your
notes about what changes this commit includes.

```{warning}
Do not underestimate the value of informative commit messages. When looking back to a repo's history of commits, looking for a change of interest, having good commit messages will be a game changer.
```

### **Push changes**

Use the following command to *push* your local changes to the remote
repository so that the two repositories can get in sync.

    git push origin [BRANCH-NAME]


### **Fetch changes**

If you suspect that new changes might be available on the remote
repository that are not synced to your local repo, you can use the command

    git fetch origin [BRANCH-NAME]

to download the new commits available on the remote (if any).
These new changes will be appended to the branch called
`origin/[BRANCH-NAME]` in your local repository.

If you want to apply them to your current branch, use the command

    git merge origin/[BRANCH-NAME]

Use the command `git pull origin/[BRANCH-NAME]` to perform *fetch*
and then *merge*.


### **Delete a branch locally and remotely**

Unlike the vast majority of git commands, the delete one does not
work on the current branch. You can delete other branches with:

    git branch -d [BRANCH-NAME]

If you want to delete your current branch, you will need to checkout
another branch first. This prevents ending up with a repository
with no branches.

To propagate the deletion of a branch to the remote repository,
run the command:

    git push origin --delete [BRANCH-NAME]

### **Open a GitHub Issue**

If you are experiencing issues with any code or content of a repository,
such as this manual, you can submit GitHub "issues" by navigating to the `Issues` tab of the desired repo and selecting _New issue_.

For example, when you find a typo or a mistake in this instruction manual,
you can (and should!) visit the [Duckietown developer manual issues page](https://github.com/duckietown/book-devmanual-docs/issues) and report an issue, so it can be reviewed and addressed.

Even better, you could fork this repo, fix the issue, and make a PR. We have a different manual with [tips and tricks on how to contribute to the Duckietown documentation system](https://docs.duckietown.com/daffy/devmanual-docs/intro.html).

GitHub Issues are a crucial part of the lifecycle of a software product, as
they provide a feedback loop that goes directly from the end-user to the  developers. You do not have to be a developer or an expert in software
engineering to open an Issue, and issue cannot "break the build", so you can dare and open issues even when you are not super confident.


## Hands-On resources

(dev-basics-git-resources)=
### Git

It is strongly recommended that all Git beginners follow this well done tutorial:

* [Learn Git Branching](https://learngitbranching.js.org/).

Further reading material can be found at the following links:

* [Git Handbook](https://guides.github.com/introduction/git-handbook/)
* [Basic Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
* [GitHub hello world](https://guides.github.com/activities/hello-world/)

(dev-basics-git-github-setup)=
### GitHub essentials

To get the ball rolling, create a (free) account at https://github.com and configure your SSH keys for password-less access:

1. [Generate a new SSH key](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
2. [Add SSH key to your GitHub account](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).


## Ask the community

If you have any questions about how to use of Git in Duckietown,
[join the Duckietown Slack community](https://duckietown.com/join-slack) and ask away.

<!--
### Keep your password stored locally

```{warning}
Follow this step only if you are working on your **personal** computer.
```

If you are setting up GitHub on your personal computer, and you use two-factor authentication, it might be time-consuming to provide credentials at every use. Instead, you can store your password on your computer with:

    git config --global credential.helper store

(prelim-sw-ssh)=
## Connect with SSH

To seamlessly access GitHub through terminal without having to enter the password each time, you can generate a SSH key pair and add it to the SSH agent. 

Follow the [SSH instructions on GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), or continue reading below.

### Checking for existing SSH keys

First, [check if you already have existing GitHub SSH keys on your computer](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys#checking-for-existing-ssh-keys):

`````{tab-set}
````{tab-item} Ubuntu
Before you generate a new SSH key, you should check your local machine for existing keys.

1. Open Terminal.

2. Run `ls -al ~/.ssh` to see if existing SSH keys are present.
    ```
    $ ls -al ~/.ssh
    # Lists the files in your .ssh directory, if they exist
    ```

3. Check the directory listing to see if you already have a public SSH key. By default, the filenames of supported public keys for GitHub are one of the following.
    * `id_rsa.pub`
    * `id_ecdsa.pub`
    * `id_ed25519.pub`

    ```{tip}
    If you receive an error that `~/.ssh` does not exist, you do not have an existing SSH key pair in the default location. You can create a new SSH key pair in the next step.
    ```

4. Either generate a new SSH key or upload an existing key.
    * If you do not have a supported public and private key pair, or do not wish to use any that are available, generate a new SSH key.
    * If you see an existing public and private key pair listed (for example, `id_rsa.pub` and `id_rsa`) that you would like to use to connect to GitHub, you can add the key to the ssh-agent.
````

````{tab-item} macOS
Before you generate a new SSH key, you should check your local machine for existing keys.

1. Open Terminal.

2. Enter `ls -al ~/.ssh` to see if existing SSH keys are present.
    ```
    $ ls -al ~/.ssh
    # Lists the files in your .ssh directory, if they exist
    ```

3. Check the directory listing to see if you already have a public SSH key. By default, the filenames of supported public keys for GitHub are one of the following.
    * `id_rsa.pub`
    * `id_ecdsa.pub`
    * `id_ed25519.pub`
    ```{tip}
    If you receive an error that `~/.ssh` does not exist, you do not have an existing SSH key pair in the default location. You can create a new SSH key pair in the next step.
    ```

4. Either generate a new SSH key or upload an existing key.
    * If you do not have a supported public and private key pair, or do not wish to use any that are available, generate a new SSH key.
    * If you see an existing public and private key pair listed (for example, `id_rsa.pub` and `id_rsa`) that you would like to use to connect to GitHub, you can add the key to the ssh-agent.
````

````{tab-item} Windows
Before you generate a new SSH key, you should check your local machine for existing keys.

1. Open Git Bash.

2. Enter `ls -al ~/.ssh` to see if existing SSH keys are present.
    ```
    $ ls -al ~/.ssh
    # Lists the files in your .ssh directory, if they exist
    ```

3. Check the directory listing to see if you already have a public SSH key. By default, the filenames of supported public keys for GitHub are one of the following.
    * `id_rsa.pub`
    * `id_ecdsa.pub`
    * `id_ed25519.pub`
    ```{tip}
    If you receive an error that `~/.ssh` does not exist, you do not have an existing SSH key pair in the default location. You can create a new SSH key pair in the next step.
    ```

4. Either generate a new SSH key or upload an existing key.
    * If you do not have a supported public and private key pair, or do not wish to use any that are available, generate a new SSH key.
    * If you see an existing public and private key pair listed (for example, `id_rsa.pub` and `id_rsa`) that you would like to use to connect to GitHub, you can add the key to the ssh-agent.
````
`````

(prelim-sw-ssh-keys)=
### Generating a new SSH key

From [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key):

``````{tab-set}
`````{tab-item} Ubuntu
You can generate a new SSH key on your local machine. After you generate the key, you can add the public key to your account on GitHub.com to enable authentication for Git operations over SSH.

1. Open Terminal.

2. Paste the text below, replacing the email used in the example with your GitHub email address.
    ```
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
    ````{note}
    If you are using a legacy system that does not support the Ed25519 algorithm, use:
    ```
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
    ````
    This creates a new SSH key, using the provided email as a label.
    ```
    > Generating public/private ALGORITHM key pair.
    ```
    When you are prompted to "Enter a file in which to save the key", you can press `Enter` to accept the default file location. Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key, in which case we recommend creating a custom-named SSH key. To do so, type the default file location and replace `id_ALGORITHM` with your custom key name.
    ```
    > Enter a file in which to save the key (/home/YOU/.ssh/id_ALGORITHM):[Press enter]
    ```

3. At the prompt, type a secure passphrase.
    ```
    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]
    ```
`````

`````{tab-item} macOS
You can generate a new SSH key on your local machine. After you generate the key, you can add the public key to your account on GitHub.com to enable authentication for Git operations over SSH.

1. Open Terminal.

2. Paste the text below, replacing the email used in the example with your GitHub email address.
    ```
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
    ````{note}
    If you are using a legacy system that does not support the Ed25519 algorithm, use:
    ```
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
    ````
    This creates a new SSH key, using the provided email as a label.
    ```
    > Generating public/private ALGORITHM key pair.
    ```
    When you are prompted to "Enter a file in which to save the key", you can press `Enter` to accept the default file location. Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key, in which case we recommend creating a custom-named SSH key. To do so, type the default file location and replace `id_ALGORITHM` with your custom key name.
    ```
    > Enter a file in which to save the key (/Users/YOU/.ssh/id_ALGORITHM):[Press enter]
    ```

3. At the prompt, type a secure passphrase.
    ```
    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]
    ```
`````

`````{tab-item} Windows
You can generate a new SSH key on your local machine. After you generate the key, you can add the public key to your account on GitHub.com to enable authentication for Git operations over SSH.

1. Open Git Bash.

2. Paste the text below, replacing the email used in the example with your GitHub email address.
    ```
    ssh-keygen -t ed25519 -C "your_email@example.com"
    ```
    ````{note}
    If you are using a legacy system that does not support the Ed25519 algorithm, use:
    ```
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
    ````
    This creates a new SSH key, using the provided email as a label.
    ```
    > Generating public/private ALGORITHM key pair.
    ```
    When you are prompted to "Enter a file in which to save the key", you can press `Enter` to accept the default file location. Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key, in which case we recommend creating a custom-named SSH key. To do so, type the default file location and replace `id_ALGORITHM` with your custom key name.
    ```
    > Enter file in which to save the key (c:\Users\YOU\.ssh\id_ALGORITHM):[Press enter]
    ```

3. At the prompt, type a secure passphrase.
    ```
    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]
    ```
`````
``````

### Adding your SSH key to the SSH agent

From [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent):

``````{tab-set}
````{tab-item} Ubuntu
Before adding a new SSH key to the ssh-agent to manage your keys, you should have checked for existing SSH keys and generated a new SSH key.

1. Start the ssh-agent in the background.
    ```
    $ eval "$(ssh-agent -s)"
    > Agent pid 59566
    ```
    Depending on your environment, you may need to use a different command. For example, you may need to use root access by running `sudo -s -H` before starting the ssh-agent, or you may need to use `exec ssh-agent bash` or `exec ssh-agent zsh` to run the ssh-agent.

2. Add your SSH private key to the ssh-agent.

    If you created your key with a different name, or if you are adding an existing key that has a different name, replace `id_ed25519` in the command with the name of your private key file.
    ```
    ssh-add ~/.ssh/id_ed25519
    ```

3. Add the SSH public key to your account on GitHub.
````

`````{tab-item} macOS
Before adding a new SSH key to the ssh-agent to manage your keys, you should have checked for existing SSH keys and generated a new SSH key. When adding your SSH key to the agent, use the default macOS `ssh-add` command, and not an application installed by [macports](https://www.macports.org/), [homebrew](https://brew.sh/), or some other external source.

1. Start the ssh-agent in the background.
    ```
    $ eval "$(ssh-agent -s)"
    > Agent pid 59566
    ```
    Depending on your environment, you may need to use a different command. For example, you may need to use root access by running `sudo -s -H` before starting the ssh-agent, or you may need to use `exec ssh-agent bash` or `exec ssh-agent zsh` to run the ssh-agent.

2. If you are using macOS Sierra 10.12.2 or later, you will need to modify your `~/.ssh/config` file to automatically load keys into the ssh-agent and store passphrases in your keychain.

    * First, check to see if your `~/.ssh/config` file exists in the default location.
    ```
    $ open ~/.ssh/config
    > The file /Users/YOU/.ssh/config does not exist.
    ```
    * If the file does not exist, create the file.
    ```
    touch ~/.ssh/config
    ```
    * Open your `~/.ssh/config` file, then modify the file to contain the following lines. If your SSH key file has a different name or path than the example code, modify the filename or path to match your current setup.
    ```
    Host github.com
      AddKeysToAgent yes
      UseKeychain yes
      IdentityFile ~/.ssh/id_ed25519
    ```
    ````{note}
    * If you chose not to add a passphrase to your key, you should omit the `UseKeychain` line.
    * If you see a `Bad configuration option: usekeychain` error, add an additional line to the configuration's' `Host *.github.com` section.
    ```
    Host github.com
      IgnoreUnknown UseKeychain
    ```
    ````

3. Add your SSH private key to the ssh-agent and store your passphrase in the keychain. If you created your key with a different name, or if you are adding an existing key that has a different name, replace `id_ed25519` in the command with the name of your private key file.
    ```
    ssh-add --apple-use-keychain ~/.ssh/id_ed25519
    ```
    ```{note}
    The `--apple-use-keychain` option stores the passphrase in your keychain for you when you add an SSH key to the ssh-agent. If you chose not to add a passphrase to your key, run the command without the `--apple-use-keychain` option.

    The `--apple-use-keychain` option is in Apple's standard version of `ssh-add`. In macOS versions prior to Monterey (12.0), the `--apple-use-keychain` and `--apple-load-keychain` flags used the syntax `-K` and `-A`, respectively.

    If you do not have Apple's standard version of `ssh-add` installed, you may receive an error.

    If you continue to be prompted for your passphrase, you may need to add the command to your `~/.zshrc` file (or your `~/.bashrc` file for bash).
    ```

4. Add the SSH public key to your account on GitHub.
`````

````{tab-item} Windows
Before adding a new SSH key to the ssh-agent to manage your keys, you should have checked for existing SSH keys and generated a new SSH key.

If you have [GitHub Desktop](https://desktop.github.com/) installed, you can use it to clone repositories and not deal with SSH keys.

1. In a new `admin elevated` PowerShell window, ensure the ssh-agent is running.
    ```
    # start the ssh-agent in the background
    Get-Service -Name ssh-agent | Set-Service -StartupType Manual
    Start-Service ssh-agent
    ```

2. In a terminal window without elevated permissions, add your SSH private key to the ssh-agent. If you created your key with a different name, or if you are adding an existing key that has a different name, replace `id_ed25519` in the command with the name of your private key file.
    ```
    ssh-add c:\Users\YOU\.ssh\id_ed25519
    ```

3. Add the SSH public key to your account on GitHub.
````
``````

### Generating a new SSH key for a hardware security key

If you want to step up your security, you can set up a hardware security key. From [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key-for-a-hardware-security-key):

``````{tab-set}
`````{tab-item} Ubuntu
If you are using macOS or Linux, you may need to update your SSH client or install a new SSH client prior to generating a new SSH key.

1. Insert your hardware security key into your computer.

2. Open Terminal.

3. Paste the text below, replacing the email address in the example with the email address associated with your account on GitHub.
    ```
    ssh-keygen -t ed25519-sk -C "your_email@example.com"
    ```
    ````{note}
    If the command fails and you receive the error `invalid format` or `feature not supported`, you may be using a hardware security key that does not support the Ed25519 algorithm. Enter the following command instead.
    ```
    ssh-keygen -t ecdsa-sk -C "your_email@example.com"
    ```
    ````

4. When you are prompted, touch the button on your hardware security key.

5. When you are prompted to "Enter a file in which to save the key," press `Enter` to accept the default file location.
    ```
    > Enter a file in which to save the key (/Users/YOU/.ssh/id_ed25519_sk):[Press enter]
    ```

6. When you are prompted to type a passphrase, press `Enter`.
    ```
    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]
    ```

7. Add the SSH public key to your account on GitHub.
`````

`````{tab-item} macOS
If you are using macOS or Linux, you may need to update your SSH client or install a new SSH client prior to generating a new SSH key.

1. Insert your hardware security key into your computer.

2. Open Terminal.

3. Paste the text below, replacing the email address in the example with the email address associated with your account on GitHub.
    ```
    ssh-keygen -t ed25519-sk -C "your_email@example.com"
    ```
    ````{note}
    If the command fails and you receive the error `invalid format` or `feature not supported`, you may be using a hardware security key that does not support the Ed25519 algorithm. Enter the following command instead.
    ```
    ssh-keygen -t ecdsa-sk -C "your_email@example.com"
    ```
    ````

4. When you are prompted, touch the button on your hardware security key.

5. When you are prompted to "Enter a file in which to save the key," press `Enter` to accept the default file location.
    ```
    > Enter a file in which to save the key (/Users/YOU/.ssh/id_ed25519_sk):[Press enter]
    ```

6. When you are prompted to type a passphrase, press `Enter`.
    ```
    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]
    ```

7. Add the SSH public key to your account on GitHub.
`````

`````{tab-item} Windows
If you are using macOS or Linux, you may need to update your SSH client or install a new SSH client prior to generating a new SSH key.

1. Insert your hardware security key into your computer.

2. Open Git Bash.

3. Paste the text below, replacing the email address in the example with the email address associated with your account on GitHub.
    ```
    ssh-keygen -t ed25519-sk -C "your_email@example.com"
    ```
    ````{note}
    If the command fails and you receive the error `invalid format` or `feature not supported`, you may be using a hardware security key that does not support the Ed25519 algorithm. Enter the following command instead.
    ```
    ssh-keygen -t ecdsa-sk -C "your_email@example.com"
    ```
    ````

4. When you are prompted, touch the button on your hardware security key.

5. When you are prompted to "Enter a file in which to save the key," press `Enter` to accept the default file location.
    ```
    > Enter a file in which to save the key (c:\Users\YOU\.ssh\id_ed25519_sk):[Press enter]
    ```

6. When you are prompted to type a passphrase, press `Enter`.
    ```
    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]
    ```

7. Add the SSH public key to your account on GitHub.
`````
``````

(prelim-sw-ssh-keys-upload)=
### Adding a new SSH key to your GitHub account

From [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account):

``````{tab-set}
````{tab-item} Ubuntu
You can add an SSH key and use it for authentication, or commit signing, or both. If you want to use the same SSH key for both authentication and signing, you need to upload it twice.

After adding a new SSH authentication key to your account on GitHub.com, you can reconfigure any local repositories to use SSH.

1. Copy the SSH public key to your clipboard.

    If your SSH public key file has a different name than the example code, modify the filename to match your current setup. When copying your key, do not add any newlines or whitespace.
    ```
    $ cat ~/.ssh/id_ed25519.pub
    # Then select and copy the contents of the id_ed25519.pub file
    # displayed in the terminal to your clipboard
    ```
    ```{tip}
    Alternatively, you can locate the hidden `.ssh` folder, open the file in your favorite text editor, and copy it to your clipboard.
    ```

2. In the upper-right corner of any page on GitHub, click your profile photo, then click `Settings`.

3. In the "Access" section of the sidebar, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-key" aria-hidden="true"><path d="M10.5 0a5.499 5.499 0 1 1-1.288 10.848l-.932.932a.749.749 0 0 1-.53.22H7v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22H5v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22h-2A1.75 1.75 0 0 1 0 14.25v-2c0-.199.079-.389.22-.53l4.932-4.932A5.5 5.5 0 0 1 10.5 0Zm-4 5.5c-.001.431.069.86.205 1.269a.75.75 0 0 1-.181.768L1.5 12.56v1.69c0 .138.112.25.25.25h1.69l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l1.023-1.025a.75.75 0 0 1 .768-.18A4 4 0 1 0 6.5 5.5ZM11 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg> `SSH and GPG keys`.

4. Click `New SSH key` or `Add SSH key`.

5. In the "Title" field, add a descriptive label for the new key. For example, if you are using a personal laptop, you might call this key "Personal laptop".

6. Select the type of key, either authentication or signing.

7. In the "Key" field, paste your public key.

8. Click `Add SSH key`.

9. If prompted, confirm access to your account on GitHub.
````

````{tab-item} macOS
You can add an SSH key and use it for authentication, or commit signing, or both. If you want to use the same SSH key for both authentication and signing, you need to upload it twice.

After adding a new SSH authentication key to your account on GitHub.com, you can reconfigure any local repositories to use SSH.

1. Copy the SSH public key to your clipboard.

    If your SSH public key file has a different name than the example code, modify the filename to match your current setup. When copying your key, do not add any newlines or whitespace.
    ```
    $ pbcopy < ~/.ssh/id_ed25519.pub
    # Copies the contents of the id_ed25519.pub file to your clipboard
    ```
    ```{tip}
    If `pbcopy` is not working, you can locate the hidden `.ssh` folder, open the file in your favorite text editor, and copy it to your clipboard.
    ```

2. In the upper-right corner of any page on GitHub, click your profile photo, then click `Settings`.

3. In the "Access" section of the sidebar, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-key" aria-hidden="true"><path d="M10.5 0a5.499 5.499 0 1 1-1.288 10.848l-.932.932a.749.749 0 0 1-.53.22H7v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22H5v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22h-2A1.75 1.75 0 0 1 0 14.25v-2c0-.199.079-.389.22-.53l4.932-4.932A5.5 5.5 0 0 1 10.5 0Zm-4 5.5c-.001.431.069.86.205 1.269a.75.75 0 0 1-.181.768L1.5 12.56v1.69c0 .138.112.25.25.25h1.69l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l1.023-1.025a.75.75 0 0 1 .768-.18A4 4 0 1 0 6.5 5.5ZM11 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg> `SSH and GPG keys`.

4. Click `New SSH key` or `Add SSH key`.

5. In the "Title" field, add a descriptive label for the new key. For example, if you are using a personal laptop, you might call this key "Personal laptop".

6. Select the type of key, either authentication or signing.

7. In the "Key" field, paste your public key.

8. Click `Add SSH key`.

9. If prompted, confirm access to your account on GitHub.
````

`````{tab-item} Windows
You can add an SSH key and use it for authentication, or commit signing, or both. If you want to use the same SSH key for both authentication and signing, you need to upload it twice.

After adding a new SSH authentication key to your account on GitHub.com, you can reconfigure any local repositories to use SSH.

1. Copy the SSH public key to your clipboard.

    If your SSH public key file has a different name than the example code, modify the filename to match your current setup. When copying your key, do not add any newlines or whitespace.
    ```
    $ clip < ~/.ssh/id_ed25519.pub
    # Copies the contents of the id_ed25519.pub file to your clipboard
    ```
    ````{note}
    * With Windows Subsystem for Linux (WSL), you can use `clip.exe`. Otherwise if `clip` is not working, you can locate the hidden `.ssh` folder, open the file in your favorite text editor, and copy it to your clipboard.
    * On newer versions of Windows that use the Windows Terminal, or anywhere else that uses the PowerShell command line, you may receive a `ParseError` stating that `The '&lt;' operator is reserved for future use.` In this case, the following alternative `clip` command should be used:
    ```
    $ cat ~/.ssh/id_ed25519.pub | clip
    # Copies the contents of the id_ed25519.pub file to your clipboard
    ```
    ````

2. In the upper-right corner of any page on GitHub, click your profile photo, then click `Settings`.

3. In the "Access" section of the sidebar, click <svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-key" aria-hidden="true"><path d="M10.5 0a5.499 5.499 0 1 1-1.288 10.848l-.932.932a.749.749 0 0 1-.53.22H7v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22H5v.75a.749.749 0 0 1-.22.53l-.5.5a.749.749 0 0 1-.53.22h-2A1.75 1.75 0 0 1 0 14.25v-2c0-.199.079-.389.22-.53l4.932-4.932A5.5 5.5 0 0 1 10.5 0Zm-4 5.5c-.001.431.069.86.205 1.269a.75.75 0 0 1-.181.768L1.5 12.56v1.69c0 .138.112.25.25.25h1.69l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l.06-.06v-1.19a.75.75 0 0 1 .75-.75h1.19l1.023-1.025a.75.75 0 0 1 .768-.18A4 4 0 1 0 6.5 5.5ZM11 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg> `SSH and GPG keys`.

4. Click `New SSH key` or `Add SSH key`.

5. In the "Title" field, add a descriptive label for the new key. For example, if you are using a personal laptop, you might call this key "Personal laptop".

6. Select the type of key, either authentication or signing.

7. In the "Key" field, paste your public key.

8. Click `Add SSH key`.

9. If prompted, confirm access to your account on GitHub.
`````
``````

### Testing your SSH connection

From [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection):

`````{tab-set}
````{tab-item} Ubuntu
1. Open Terminal.

2. Enter the following:
    ```
    ssh -T git@github.com
    # Attempts to ssh to GitHub
    ```
    You may see a warning like this:
    ```
    > The authenticity of host 'github.com (IP ADDRESS)' can't be established.
    > ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
    > Are you sure you want to continue connecting (yes/no)?
    ```

3. Verify that the fingerprint in the message you see matches [GitHub's public key fingerprint](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints). If it does, then type `yes`:
    ```
    > Hi USERNAME! You have successfully authenticated, but GitHub does not
    > provide shell access.
    ```
    You may see this error message:
    ```
    ...
    Agent admitted failure to sign using the key.
    debug1: No more authentication methods to try.
    Permission denied (publickey).
    ```
    This is a known problem with certain Linux distributions.
    ```{note}
    The remote command should exit with code 1.
    ```

4. Verify that the resulting message contains your username.
````

````{tab-item} macOS
1. Open Terminal.

2. Enter the following:
    ```
    ssh -T git@github.com
    # Attempts to ssh to GitHub
    ```
    You may see a warning like this:
    ```
    > The authenticity of host 'github.com (IP ADDRESS)' can't be established.
    > ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
    > Are you sure you want to continue connecting (yes/no)?
    ```

3. Verify that the fingerprint in the message you see matches [GitHub's public key fingerprint](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints). If it does, then type `yes`:
    ```
    > Hi USERNAME! You have successfully authenticated, but GitHub does not
    > provide shell access.
    ```
    ```{note}
    The remote command should exit with code 1.
    ```

4. Verify that the resulting message contains your username.
````

````{tab-item} Windows
1. Open Git Bash.

2. Enter the following:
    ```
    ssh -T git@github.com
    # Attempts to ssh to GitHub
    ```
    You may see a warning like this:
    ```
    > The authenticity of host 'github.com (IP ADDRESS)' can't be established.
    > ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
    > Are you sure you want to continue connecting (yes/no)?
    ```

3. Verify that the fingerprint in the message you see matches [GitHub's public key fingerprint](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints). If it does, then type `yes`:
    ```
    > Hi USERNAME! You have successfully authenticated, but GitHub does not
    > provide shell access.
    ```
    ```{note}
    The remote command should exit with code 1.
    ```

4. Verify that the resulting message contains your username.
````
`````

```{seealso}
If you have never heard of Git or GitHub before, you can do some background reading here:

* See: [GitHub Hello World](https://guides.github.com/activities/hello-world/)

* See: [GitHub Documentation](https://guides.github.com/introduction/Llow/)

You can then go through the [Duckietown introduction to version control with Git](sec:developer_basics_git).
```