# Poetry

[Poetry] is a package manager that unifies several tasks like dependency management or building and publishing your package. It enables you to define your dependencies precisely. Consequently, another user can be sure to have the same environment as you.

To Conclude [Poetry] centralizes a large part of package management that before was distributed over several packages and files.

In this adorable [Poetry tutorial] one gets an overview and a first hand on how to use [Poetry].

## pyproject.toml

In this file, one defines the dependencies and information for a Python project. It can look like this:

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

The advantage over the classical `requirements.txt` file is that one can define separate dependencies for development and package building.

[Poetry tutorial]: https://realpython.com/dependency-management-python-poetry/
[Poetry]: https://python-poetry.org/
