# Week 1: Getting Started

- In this week, we will set up the development environment for this module.
- We will use Git, Python (with virtual environments), PyCharm (IDE), and Jupyter Notebooks.
- Follow the instructions below to set up your development environment (without cloning this repository).
- If you are confident about Git, Python virtual envs, IDEs, and Jupyter Notebooks, jump to Section 5. 


Jump to:
- [Week 1: Getting Started](#week-1-getting-started)
  - [1. Git](#1-git)
  - [2. Python \& Virtual Environments](#2-python--virtual-environments)
  - [3. PyCharm (IDE)](#3-pycharm-ide)
  - [4. Jupyter Notebooks](#4-jupyter-notebooks)
  - [5. Simple Exercise](#5-simple-exercise)


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


## 2. Python & Virtual Environments

### Getting started

Virtual environments are a way to create isolated Python environments for different projects.

To make it simple, we will use Pythons inbuilt [`venv`](https://docs.python.org/3/library/venv.html) module to create our Python virtual environments.
- All the instructions in the following weeks will be based on `venv` for Python 3.12
- If you feel confident enough, you can use other tools, such as `anaconda` or `uv`, to manage Python dependencies but please checkout the [FAQ](#virtual-environments-faq)
  
Since we will use Python in this module, we need to install Python if not yet installed.
You can check this by running the following command in your terminal:

```bash
python --version
```

If you get an error, you should install Python: https://www.python.org/downloads/

Otherwise, you are ready to use `venv`. 

Virtual enviroments or (venvs) keeps project dependencies i.e., pakcages installed by `pip install` separated from the system Python and other venvs.

To create a new venv, you can run the following command in your terminal:

```bash
python -m venv .venv
```

Once your venv is created, you can activate it by running the following command:

```sh
source .venv/bin/activate # On Linux/Mac
```

```ps 
.venv\Scripts\Activate # On Windows
```
To verify if your venv is active you can run:
```sh
which python # On Linux/Mac
```
```ps
where python # On Windows
```

It should return the path to the Python executable in your venv, which is usually something like `yourdirectory/.venv/bin/python` (Linux/Mac) or `yourdirectory\.venv\Scripts\python.exe` (Windows).

> [!NOTE]
> If you use PyCharm (see below), you probably don't need to manually create and manage `venv`; PyCharm should do it for you.

Once the venv has been activated, you can install Python packages using `pip install`:
```sh
pip install jupyter # Needed to run jupyter notebooks
```
For most lab materials, we will provide a `requirements.txt` file, which lists all the required Python packages for the lab session. To install them run:

```sh
pip install -r requirements.txt
```

For more information about `venv`, refer to the official documentation: https://docs.python.org/3/library/venv.html

### Virtual environments FAQ

#### When do I need to use virtual environments?
You should always use a virtual environment for your Python projects, especially when you have multiple project.


#### What happens if I DON'T use virtual environments?
You will install Python packages system-wide, which may cause conflicts between different projects, other system installs, and even your operating system. It is difficult to debug if things go wrong.
With virtual environments, you can always delete the `.venv` folder and start fresh.


#### Can I use the same venv for multiple projects?
You can, but it's not recommended. A clean approach is to create a new venv for each project.


#### I don't have Python 3.12 installed, can I use other versions of Python?
You should be fine with any Python >3.11 but we tested all the code in this module with Python 3.12.

#### The legacy code base I want to run is requiring different Python version, what should I do?

You have two options:
- You can install requested python version and create a venv with that python version.
- You can use `conda` or `uv` to manage multiple python versions and create venvs with different python versions.
  
#### Why not use `conda` or `uv` to manage Python dependencies?
- `conda` is a heavyweight dependency, usually not needed for most Python projects.
- `uv` is a new promissing tool but it doesn't support legacy python versions <3.8, which may be required for the module.

#### I messed up my installation, what should I do?
First delete the `.venv` folder and start over, create a fresh venv and install the required packages again.

Ask demonstrators for help.




## 3. PyCharm (IDE)

PyCharm is an IDE (Integrated Development Environment) for Python.
- If you feel comfortable with other editors, such as VSCode, you can use them instead and skip the rest of this section.
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
- If you are already familiar with Jupyter Notebooks, you can skip the rest of this section.

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
