# Poetry

Poetry is a package manager that unifies several tasks. It enables you to define your dependencies presisly. Such that another user can be sure to have the same environment as you.

In this very nice [Poetry tutorial] one gets an overview and a first hands on how to use Poetry.

## pyproject.toml

In here one defines the dependencies as well as informations for a Python project. It can look like:

```toml
# pyproject.toml

[tool.poetry]
name = "rp-poetry"
version = "0.1.0"
description = ""
authors = ["Philipp <philipp@realpython.com>"]


[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

The advantage over the classical `requirements.txt`file it that one can define seperate dependencies for development and package building. But thats not all [Poetry] also takes care of several other tasks like environment management or Testing.

[Poetry tutorial]: https://realpython.com/dependency-management-python-poetry/
