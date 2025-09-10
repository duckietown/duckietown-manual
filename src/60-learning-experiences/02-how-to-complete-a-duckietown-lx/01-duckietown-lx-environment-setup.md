```{seo}
:description: Set up your development environment for Duckietown Learning Experiences with Docker, SSL certificates, and the Duckietown shell.
:keywords: Duckietown, environment setup, LX, docker, development environment, duckietown shell, SSL, hello-world
```

```{needget}
* Computer Setup: [](setup-computer)
* Accounts: [](dt-account)
* Software prerequisites: [](setup-sw-intro)
---
*
```


(env-setup)=
# Step 1: Environment Setup

Before working through any Duckietown Learning Experience, set up your development environment.

```{important}
Complete the following setup steps carefully to prevent running into bugs later on.
```

## LX Prerequisites

If you have not done so already, set up your Duckietown software environment:

* Computer Setup: [](setup-computer)
* Accounts: [](dt-account)
* Software prerequisites: [](setup-sw-intro)

Then, install the following dependency libraries:

`````{tab-set}
````{tab-item} Linux
Open a terminal and run the following command:
```bash
sudo apt install libnss3-tools
```
````

````{tab-item} macOS
Open a terminal and run the following command:
```bash
brew install nss
```
````

````{tab-item} Windows
No need to install dependencies if you are running Windows.
````
`````

Then, update the Duckietown shell and the Duckietown Shell commands:

```bash
pipx upgrade duckietown-shell
dts update
```

## LX Docker Configuration

After completing the preliminary setup and bringing your system up to date, add your `docker.io` credentials to the Duckietown Shell:

```bash
dts challenges config --docker-username <USERNAME> --docker-password <PASSWORD>
```

```{note}
These are the `<USERNAME>` and `<PASSWORD>` that you use to log in to DockerHub (hub.docker.io) when 
setting up Docker in the Duckiebot operation manual.
```

(lx-ssl-certificate-setup)=
## SSL certificate

We use SSL certificates and TLS encryption to guarantee the highest standard of safety and privacy. Set up a local SSL certificate needed to run the LX editor inside your browser:

```bash
dts setup mkcert
```

## 4 - The `hello-world` LX

```{todo}
Bring hello-world LX instructions up to date with ente
```

Fork and clone the [`duckietown-lx`](https://github.com/duckietown/duckietown-lx) repository to follow along and complete the tutorial activities. 

This will give you access to the full library of Duckietown Learning Experiences.

1) To store your code, while also keeping the ability to pull updates from our version of this repository, create your own fork. Start by pressing "Fork" in the top right corner of [the duckietown-lx repository page on GitHub](https://github.com/duckietown/duckietown-lx). 
   Your new repository fork will appear in your GitHub repository list as: 

        <your_username>/duckietown-lx

    Then clone your new repository, replacing your GitHub username in the command below:
    
```bash
git clone -b mooc2022 git@github.com:<your_username>/duckietown-lx
```

2) Configure the Duckietown version of this repository as the upstream repository to synchronize with your fork. Navigate to the repository folder and then list the current remote repository for your fork:

```bash
git remote -v
```

    Specify a new remote upstream repository:

```bash
git remote add upstream https://github.com/duckietown/duckietown-lx
```

    Confirm that the new upstream repository was added to the list:

```bash
git remote -v
```

    You can now push your work to your repository using the standard GitHub workflow, and the beginning of every learning experience will prompt you to pull from the upstream repository - updating your exercises to the latest Duckietown version:

```bash
git pull upstream mooc2022
```

You are now ready to move on to the next section and start your development journey with the `dts code` workflow.
