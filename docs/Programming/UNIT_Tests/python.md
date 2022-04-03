# UNIT tests in Python

First of all, there is a folder `test` in parallel to the source-code folder of the Python package, containing all testing files. In this folder, we add a `README.md` file explaining how the tests are structured.

## test-functions

- `AssertEqual-function`: compare a return value of a function/class with a expected value
- If we test only on exceptions: `Assert(True)`
- If we want to test on a special exception, we use assertions about expected exceptions
- `setup function: To prepare for the tests, for example, provide access to a database. The setup function runs at first.
- `TearDown-function`: Diminish the test resources after the tests, for example, to cut the connection to a database.

## Call of tests

We call tests via the command line. Thereby we can select which tests should run and also skip tests. Later is helpful if the package is not developed enough to execute a particular test.

## Test results

The results are presented in a `JUnitXML`-file, which can be opened in a browser window. Thereof we get a graphical response about the test results.

## How to organize the expected values of the tests

### Parameterization of test-functions

For n test values (e.g., by a limiter), it makes sense to parameterize the test functions. The test cases can be created in the test modules or separate parameter files. Parameterization has the advantage that it is immediately visible which test has failed in case of an error.

### Usage of test-classes

Test classes are mainly for test organization. Therefore one understands, which test functions are connected since they are collected in one class.

## Test types

- Limit-tests: Execute value below lower border and above upper border as test
- sign-test

## Testing in Python

The absolute standard package is the `Pytest`-package. `Pytest` contains the following components:

- there is a **test folder**
- there is a **test runner**
- `Conftest.py` configures the tests
- **Pytest fixture (deocrator)**: Test preparation and clean up for code
- **Test-files**: module names all have the prefix `test` in their filenames
- **Test-functions**: Function-names also have the prefix `test`. The rest of the name should be as descriptive as possible.
- tests can be parameterized

## Test coverage

One can use tools like [Codecov] to measure the test-coverage of your code. It runs through all your source code files and checks which lines are covered by the tests you have written so far. Thereoff you can detect potential weaknesses in your code.

To learn more one can have a look at this more [general but excelent tutorial]

[general but excelent tutorial]: https://www.earthdatascience.org/blog/unit-testing-linting-ci-python/
[Codecov]: https://docs.codecov.com/docs
