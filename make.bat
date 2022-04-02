@ECHO OFF

REM Command file
if "%1" == "" goto help

if "%1" == "help" (
    :help
    echo.Please use `make ^<target^>` where ^<target^> is one of
    echo.  docs   to build the HTML documentation
    goto end
)

if "%1" == "docs" (
    cd docs
    make html
    cd ..
    goto end
)

:end
