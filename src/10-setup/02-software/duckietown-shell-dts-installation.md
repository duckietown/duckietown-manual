```{seo}
:description: How to install and set up the Duckietown Shell, the terminal based and most powerful UI in Duckietown.
:keywords: Duckietown, Duckiebot, dts, Duckietown Shell, UI, terminal interface
```

(setup-dts)=
# Duckietown Shell (`dts`)

This section describes how to install and set up `dts` (`Duckietown Shell`), a CLI (Command-Line Interface) program that is used for Duckietown-related operations.

```{needget}
- [Docker is installed and set up](setup-sw-docker)

- [GitHub is installed and set up](setup-sw-github)

- [Duckietown account](setup-account-duckietown-hub)

- [Software dependencies, including pipx](setup-sw-dependencies)
---
- A computer with `dts` installed and correctly set up.
```

(setup-dts-installation)=
## Duckietown Shell (`dts`) Installation

DTS requires __CPython 3.10, 3.11, or 3.12__ and supports Linux x86-64/ARM64, macOS Intel/Apple Silicon, and Windows x86-64. Other Python versions and platforms are not supported.

Use an already-installed, supported interpreter. The examples select Python 3.12 explicitly; replace `python3.12` with `python3.10` or `python3.11` if that is the supported interpreter installed on your computer. Host installation instructions for macOS and Windows are in [](dts-install-host-machine).

:::::{tab-set}

::::{tab-item} Ubuntu

````{attention}
If you have already installed `dts` using `pip3`, run the following command and follow the on-screen instructions:

```shell
pip3 uninstall duckietown-shell
```
````

To install `dts`, run:

```shell
pipx install --python python3.12 duckietown-shell
```

::::

::::{tab-item} Duckietown Workspace

The Duckietown Shell is pre-installed in Workspaces. Run the checkpoint to verify it is working as intended. An optional host installation is separate; follow [](dts-install-host-machine) to install and configure it.

::::

:::::

````{warning}
Some DTS commands need additional dependencies that require build tools on ARM-based Ubuntu computers, including Ubuntu virtual machines on Apple Silicon Macs:

```shell
sudo apt install -y gcc python3-dev
```

The development headers must match the Python interpreter used by DTS. Installing a compiler does not make an unsupported Python version or platform compatible with DTS.
````

(setup-dts-checkpoint1)=
### Checkpoint 1 ✅

To verify that `dts` has been installed correctly:

````{testexpect}
Run:

```shell
which dts
---
The path to `dts`.
````

(setup-dts-configuration)=
## Duckietown Shell (`dts`) configuration

To appropriately configure the Duckietown Shell:

1. [Login into `dts` as a Duckietown User](dt-account-set-token)

2. [Provide `dts` with your DockerHub credentials](dt-account-dockerhub-config-docker-set)

(dt-account-set-token)=
### Logging in the Duckietown Shell

To log into `dts` with your user configurations:

1. Open a terminal and run `dts`.

2. Select `ente` using <kbd>UpArrow</kbd> and <kbd>DownArrow</kbd>.

3. Press <kbd>Enter</kbd>.

4. Obtain and copy your [Duckietown token](duckietown-token).

5. Paste your `dt2` token into the terminal.

6. Press <kbd>Enter</kbd>.

7. Run `dts update`.

````{note}
The resulting output after step 6 should look like the following, where `UID` is your Duckietown UID (User ID):

```shell
dts :  Correctly identified as uid = UID
```
````

(setup-dts-plans)=
### Plans and computer access

The following access rules apply to `ente` and Duckiematrix:

- From __1 February 2027 at 00:00 UTC__, `ente` and `ente-staging` require the free __Independent User__ plan or an active __Institutional User__ plan. The __Instructor__ add-on alone is not sufficient. See [](duckietown-plans) to choose a plan.

- Before that deadline, active accounts can use `ente` and Duckiematrix without a qualifying plan. You still need to sign in, and the one-computer limit applies.

- `daffy` and `daffy-staging` remain plan-free. Generating an ordinary Duckietown identity token does not require a plan.

- Active Hub staff and superusers are exempt from the plan and one-computer limits.

To inspect your account plans, access eligibility, registered computer, and any pending transfer, run:

```shell
dts plan status
```

Each account that is neither staff nor a superuser can register one DTS computer. DTS registers your computer automatically when it first approves access to `ente`. A virtual machine, a separate operating-system installation, or reinstalling the operating system may count as a different computer.

A [Duckietown Workspace](setup-devcontainer) and DTS on its host share one computer registration when the Workspace is created from the same operating system where host DTS runs. Sign in separately in each installation using the same Duckietown account. See [](setup-devcontainer-shared-computer) for setup and instructions for older Workspaces.

When moving to a replacement computer, run this command __on the replacement computer__:

```shell
dts plan transfer
```

A transfer may be immediate or scheduled for after all previously issued authorizations expire, for at most 24 hours. While a transfer is pending, new authorizations are paused. `dts plan status` shows when the replacement computer can request access. Switching profiles, copying tokens, or resetting local settings does not reset this per-account registration.

After using `ente` online on your registered computer, you can continue using it offline until your saved access expires, for at most 24 hours. Access may end sooner if your qualifying plan expires or the grace period ends. Connect to the internet to renew expired access. `daffy` does not require a plan, although individual commands may still need network access.

Token, profile, command-management, and plan-management commands remain available when `ente` access is denied.

(dt-account-switch)=
### Switching user in the Duckietown Shell

To switch the user logged in to `dts`, run:

```shell
dts tok set
```

To verify which user is logged in:

```shell
dts tok status
```

(dt-account-switch-profile)=
### Duckietown Shell (`dts`) profiles

To get a list of the available `dts` profiles, run:

```shell
dts profile list
```

The output lists the available profiles. For example:

```text
   | Profile | Distribution | Staging
-- | ------- | ------------ | -------
>> |    ente |         ente |      No
```

To create a new `dts` profile:

1. Run `dts profile new`.

2. Select the name of the profile to create using <kbd>UpArrow</kbd> and <kbd>DownArrow</kbd>.

3. Press <kbd>Enter</kbd>.

4. Obtain and copy your [Duckietown token](duckietown-token).

5. Paste your `dt2` token into the terminal.

6. Press <kbd>Enter</kbd>.

To switch to a different `dts` profile, run the following command, where `PROFILE` is the name of the profile:

```shell
dts profile switch PROFILE
```

(dt-account-dockerhub-config-docker-set)=
### Configure Docker in the Duckietown Shell

To automate most back-end operations involving Docker, run:

```shell
dts config docker credentials set --username DOCKERHUB_USERNAME --password DOCKERHUB_ACCESS_TOKEN
```

Before running it:

- Recall your `DOCKERHUB_USERNAME` from [](dt-account-dockerhub).

- Create a PAT following the [Docker Hub instructions on access tokens](https://docs.docker.com/security/access-tokens/).

```{attention}
- These credentials are __only stored locally__;

- __Never use your account password__ instead of a personal access token (PAT).
```

```{admonition} For developers
:class: dropdown

With an extra __positional__ argument, one could specify a custom Docker registry server other than
`docker.io`. Check `dts config docker set --help` for more details.
```

(setup-dts-updating)=
### Updating the Shell and its commands

For a pipx installation, update the installed Shell package and then its command sets:

```shell
pipx upgrade duckietown-shell
dts update
dts version
```

`pipx upgrade` updates the Shell package; `dts update` updates command sets, not the package itself. To recreate an existing pipx installation with a supported interpreter, use `pipx reinstall --python python3.12 duckietown-shell`.

Use `dts update` for every distribution, including `daffy`. DTS verifies each downloaded update before installing it; do not modify the installed command files.

### Resetting the Duckietown Shell

```{warning}
A full reset removes your profiles, saved login, Docker credentials, and offline access. Make sure you can retrieve your Duckietown token and Docker credentials before continuing. Resetting local settings does not free your registered computer; use `dts plan transfer` when moving to another computer.
```

To reset `dts` to "factory conditions", run:

```shell
rm -rf ~/.duckietown/shell
```

and proceed to reconfigure your `dts`: [](dt-account-set-token).

---

### Checkpoint 2 ✅

```{tip}
Never skip a checkpoint!\
If you have trouble with any of these commands, see the FAQs section below. If you cannot find answers, use the Duckietown support channels to get help.
```

````{testexpect}
If your Docker login was successful, you should be able to run:

```shell
dts config docker credentials info
---
You should see an output similar to the following,

```text
Docker credentials:
. registry:   docker.io
. username:   DOCKERHUB_USERNAME
. secret:   DOCKERHUB_ACCESS_TOKEN
````

<!--
(dt-account-dockerhub-shell-credentials)=
### 1) Configure the Duckietown Shell

The first thing you need to do with `dts` is to set the Duckietown software distribution you want to work with.
For this version of the book, we use daffy. Set the shell to use a profile on the daffy distribution by running the command

    dts profile switch daffy

(dt-account-register)=
### 2) Get a Duckietown Token

Now your Duckietown Shell needs a Duckietown token. The Duckietown Token allows you to authenticate yourself and your robots against the Duckietown network.

You can make a Duckietown account for free from the Duckietown Hub.
[Make an account here.](https://hub.duckietown.com/signup/)

The token is a string of letters and numbers that looks something like this:

    dt1-7vEuJsaxeXXXXX-43dzqWFnWd8KBa1yev1g3UKnzVxZkkTbfSJnxzuJjWaANeMf4y6XSXBWTpJ7vWXXXX

To find your token, first [log in](https://hub.duckietown.com/signin/) to your account,
then open [the profile page](https://hub.duckietown.com/profile/) in your browser:

Copy your token to use in the next step.
-->

### Troubleshooting

```{trouble}
I mistakenly set a wrong/unwanted username or password. How can I update the credentials?
---
Just run the command again with the correct credentials.
Only the latest inputs are stored for the same Docker registry.
```

```{trouble}
I would like to remove my stored Docker credentials. How could I achieve that?
---
Run: 

~~~shell
rm ~/.duckietown/shell/profiles/ente/databases/secrets_docker.yaml
~~~
```
