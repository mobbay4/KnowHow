# Git Hooks

Git hooks are tasks (like in the GitLab CI/CD) that are executed before a commit. This is useful to for example test for certain requirements before a commit is fulfilled. This becomes exspeacially handy for linting and testing tasks. Such as using [pytest] or [black]. To implement git-hooks one uses the [pre-commit] Python package to use common hooks in a simple way. But there is also the posibility to implement own git hooks in bash logic. Sadly there is no experience on custom git hooks so far. The following sections explain the general configurations and how to run certain hooks using [pre-commit].

## General configuration

To configure pre-commit please follow one of these tutorials:

- [git-hook-tutorial-1]
- [git-hook-tutorial-2]

By doing so several observations have been made that may helpful to you. First of all to use the [pre-commit] command its strongly recomended to install it in an virtual environment since otherwise the command can not be found. After the `.pre-commit-config.yaml` file is installed once the git hooks apply automatically on every commit in the git repository.

### Step by step guide

So to create a git-hook configuration for an git repository I would do the **following steps** (in an cmd terminal):

- create a fresh virtual-environment, activate and install pre-commit with:

  ```bash
  python -m virtualenv venv
  venv\Scripts\activate
  pip install pre-commit
  ```

- create a `.pre-commit-config.yaml` (template in the end of this chapter) and install it to the git-repository with:

  ```bash
  pre-commit install
  ```

- Now the defined git-hooks should apply on each commit

Here you can find an [overview of all available hooks].
In the next section one can see how to insert the specified hooks.

For me it was very usefull to use the following command that allows to apply the git hooks on all repository files:

```bash
pre-commit run --all-files
```

## Example Configuration

The next code block shows an example how one can define the `.pre-commit-config.yaml` file. The corresponding tools are shortly explained in the following subsections. In general [pre-commit] takes care about the installation and configuration of the tools. So a pip install or similar is not nessesary to use git-hooks.

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.1.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-json
      - id: check-yaml
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.5.0
    hooks:
      - id: check-added-large-files
  - repo: https://github.com/pycqa/isort
    rev: 5.5.4
    hooks:
    - id: isort
      files: "\\.(py)$"
      args: [--settings-path=pyproject.toml]
  - repo: https://github.com/psf/black
    rev: 19.10b0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 4.0.1
    hooks:
      - id: flake8
        additional_dependencies: [flake8-typing-imports==1.12.0]
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.31.1
    hooks:
    - id: markdownlint-fix
  - repo: https://github.com/editorconfig-checker/editorconfig-checker.python
    rev: 2.4.0  # pick a git hash / tag to point to
    hooks:
    - id: editorconfig-checker
      alias: ec
```

### Markdownlint-cli

The [Markdownlint-cli] hook parses over all `.md` files and checks if the recomended syntax is used. When the `-fix` option is used, simple errors like missing spacings are fixed automatically. The `.markdownlint.jsonc` file is used configure the tool. In there one can exclude certain rules (like line length limitation). We normally also introduce the [Markdownlint-cli] in the GitLab CI/CD to gain an overview on all `.md` files.

### black

[black] is a Python package that autoformates Python code to a certain standard. Thereby no functional changes are made but rather optical like additional spacings and identing. [black] is very useful since it makes the code very readable.

### flake8

[flake8] checks the code for the PEP8 standard and gives succetions where the code should be modified. This can reveal weaknesses in the code and can even teach a programmer important details. [flake8] is configured by the `.flake8` file.

### editorconfig-checker

The [eclint] tool reads the `.editorconfig` file and checks if all files in the repository apply to this standard. For deviations it gives feedback for the developer. [eclint] is configured by the `.ecrc` file.

### isort

[isort] sorts the imports of an Python module in alphabetic order.

### pre-commit-hooks

pre-commit-hooks are pre-commit native hooks that excecute mostly very simple tasks. We currently use the following:

- trailing-whitespace
- end-of-file-fixer
- check-json
- check-yaml

### check-added-large-files

Checks if there are files larger than 5 MB. Since GitLab reposetories are not intended to save large files in them. GitLab storage is very expencive!!

[black]: https://pypi.org/project/black/
[eclint]: https://www.npmjs.com/package/eclint
[git-hook-tutorial-1]: https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/
[git-hook-tutorial-2]: https://www.architecture-performance.fr/ap_blog/some-pre-commit-git-hooks-for-python/
[Markdownlint-cli]: https://github.com/igorshubovych/markdownlint-cli
[overview of all available hooks]: https://pre-commit.com/hooks.html
[pre-commit]: https://pre-commit.com/
[pytest]: https://pypi.org/project/pytest/
