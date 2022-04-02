# Getting Started

The following explains how to set up the local environment to write and deploy the documentation.

## Environment Setup

First of all, we need to clone the repository structure locally. For the moment, it is intended to have the following **local folder structure**:

```
Know_How
└─── master   # folder containing clone of master branch
└─── gh-pages # folder containing clone of gh-pages branch
```

We want folders for the two branches since if we want to deploy our documentation on GitLab, we need to build it locally and push it to the gh-pages branch. The documentation deployment is explained in the next section.

So to introduce this local environment, we perform **following steps**:

- create a folder `Know_How`
- in the latter folder, clone the repository twice and rename cloned folders to `master` and `gh-pages`
- then move into the `gh-pages` folder
  - execute the command `$ git checkout gh-pages` for switching to the right branch
- Now we move to the `master` folder
  - execute `pip install virtualenv`
  - create an virtual environment with `$ virtualenv venv` (may `$ python -m virtualenv venv`)
  - activate the environment with `$ source venv/bin/activate`
  - install the requirements with `$ pip install -r requirements.txt`
  - configure the git hooks with `$ pre-commit install`

Now the basic setup is done. The git-hooks are executed before every commit in the master branch. So it is recommended to commit before deploying the documentation. One can apply the git-hooks on all repository files with:

- `$ pre-commit run --all-files`

## Deploy the Documentation

We need to build and push the static HTML to the `gh-pages` branch to deploy the documentation. With the above described set up this process is (at least a bit simplified) by the `deploy.sh` script. Move to the `gh-pages` folder and execute `bash deploy.sh`. This automatically builds, moves, and pushes the documentation to the correct branch.

## Add Content to the Documentation

The add content, one has to modify the files in the `/docs` folder in the master branch. Just add to existing files or create new ones and add your content. To add new files, one must also adjust the `nav` section in the `mkdocs.yml` file.
