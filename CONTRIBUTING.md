# Contributing

## GitHub

### Issues
We are using GitHub issues to keep track of project during development. Each small feature/bug-fix will have its own issue.

### Merging code
Pushing code to the `master` branch has been blocked. So in order to merge your code in with the `master` branch follow these steps:

1. Either find the GitHub issue you are working on or open a new issue on GitHub
2. Create a new branch based off `master` with the following formatting: `[issue-tag]-[issue-number]` (e.g. `fix-2` or `feature-8`)
3. Commit to the new branch and work off it.
    * Make sure to push your branch to `origin`, that is push it to GitHub
4. Open a pull request, once you have finished the issue.
5. Wait for approval or revisions
  * A pull request requires at least one administrator approval to merge ino `master`

## Python
Install the newest version of python from [this link]("https://www.python.org/downloads/") if you do not already have it.

## Virtual Environments
Use `virtualenv`s to manage dependencies. 

This ensures the piloting software runs the same in everyone's development environment. It also prevents package conflicts when working with various python projects.

Run `python3 -m venv venv` in the project directory to create a virtual environment    
* This will prompt you to install the virtualenv package if you have not installed it before

Run `source venv/bin/activate` in the project directory to enter the virtualenv.

Run `pip install -r requirements.txt` to install the dependencies for the piloting software

** NOTE: PyCharm will take care of all of this by default as you set up a new project **

## IDE
I highly recommend using PyCharm because it will handle creating virtual environments, installing dependencies, git, Python related tools (such as profiling, debugging, and unit testing), and more because it is built only for Python development. It will make it easier for everyone down the road. 
