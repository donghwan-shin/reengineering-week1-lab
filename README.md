# Week 1: Getting Started

- In this week, we will set up the development environment for this module.
- We will use Git, Python (with virtual environments), PyCharm (IDE), and Jupyter Notebooks.
- Follow the instructions below to set up your development environment (without cloning this repository).
- If you are confident about Git, Python virtual envs, IDEs, and Jypyter Notebooks, jump to Section 5. 


Jump to:
- [1. Git](#1-git)
- [2. Python Virtual Envs](#2-Python-Virtual-Environments)
- [3. PyCharm (IDE)](#3-PyCharm-IDE)
- [4. Jupyter Notebooks](#4-Jupyter-Notebooks)
- [5. Simple Exercise](#5-Simple-Exercise)


## 1. Git

To use resources from GitHub, we need to install Git if not yet installed.
To check if your machine has Git installed, run the following command in your terminal:

```bash
git --version
```

If you get an error, you should install Git.

### How to Install Git (5-10 minutes)
You can download Git from [here](https://git-scm.com/downloads).
Simply download the installer for your operating system and follow the instructions.



## 2. Python Virtual Environments

To make it simple, we will use `venv` to manage our Python virtual environments.
- If you feel confident enough, you can use other tools, such as `anaconda`, and skip the rest of this section.
- However, all the instructions in the following weeks will be based on `venv`.

Since we will use Python in this module, we need to install Python if not yet installed.
You can check this by running the following command in your terminal:

```bash
python --version
```

If you get an error, you should install Python: https://www.python.org/downloads/

Otherwise, you are ready to use `venv`. 

> The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available. (from the [official Python3 venv documentation](https://docs.python.org/3/library/venv.html))

Check out [Creating virtual environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
and [How venvs work](https://docs.python.org/3/library/venv.html#how-venvs-work). 

If you use PyCharm (see below), you don't need to manually create and manage `venv`; PyCharm will do it for you.


## 3. PyCharm (IDE)

PyCharm is an IDE (Integrated Development Environment) for Python.
- If you feel comfortable with other IDEs, such as VS Code, you can use them instead and skip the rest of this section.
- However, we will use PyCharm in this module, and all the instructions will be based on PyCharm.

### How to Install PyCharm (5-10 minutes)
As a student, you are eligible for a free PyCharm Professional license.
You can find more information [here](https://www.jetbrains.com/community/education/#students).

After getting the education license, you can download PyCharm Professional from [here](https://www.jetbrains.com/pycharm/download).

After installing PyCharm, you need to restart your computer.


### How to Use PyCharm

To quickly overview PyCharm, see [Quick Start Guide](https://www.jetbrains.com/help/pycharm/getting-started.html).

You can refer to [Create and Run Your First Project](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html) to get more detailed guidelines to create and run a project in PyCharm.

As an exercise, clone this repository to your local machine and open it in PyCharm.
While you are opening the repository, PyCharm will ask you to create a Python virtual environment.
You can simply click "Create" to let PyCharm create a project-specific Python virtual environment for you.
You can then run the `hello.py` script to check if everything works well.


## 4. Jupyter Notebooks

Jupyter Notebook is a web-based interactive development environment.
- If you are already familiar with Jupyther Notebooks, you can skip the rest of this section.

Often we will give you a Jupiter Notebook file (`.ipynb`) for each hands-on exercise.
You should know how to run a Jupyter Notebook file.

In fact, it's simple. You can simply double-click a Jupyter Notebook file to open it in PyCharm.
Then, you can run each cell by clicking the "Run" button on the left side of the cell.

However, before you do anything, you should first install `jupyter` in your Python virtual environment.
PyCharm will ask you to install `jupyter` if you try to run a Jupyter Notebook file without `jupyter` installed.
You can simply click "Install Jupyter" to let PyCharm sorts it out for you.
Alternatively, you can install `jupyter` manually by running the following command in your terminal (after activating your Python virtual environment; this is done automatically in PyCharm, but you should do it manually in your terminal):

```bash
pip install jupyter
```

Note that you must activate your working Python virtual environment before installing `jupyter`.

Enjoy running Jupyter Notebook files in PyCharm!


## 5. Simple Exercise

Now, you have set up your development environment.

To check if everything works well, please *only* edit line 2 of `hello.py` to print `Hello Reengineering`.
Then, run the script and check if it is printed correctly.

![img.png](misc/img7.png)

Finally, push your code to your repository, so we can see if you've done it.
To commit and push your change, you can use either PyCharm or your terminal.

In the build-in terminal, you can run the following commands:

```bash
git add hello.py
git commit -m "Change the print message"
git push
```

Done! You have completed the first week's exercise.
