# Poetry C Extension Example

Example Python package that includes both a bit of C code and a bit of Python code.  Uses [Poetry](https://python-poetry.org/).

This repo is based on: https://github.com/Lucky-Mano/Poetry_C_Extension_Example

## Overview

This repository creates the `bobtest` python package that contains the following:

```
import bobtest

# system() is implemented in C and just execs the given command.  The example below returns the directory listing
bobtest.system.('ls')

# greeting() is implemented in Pyhton and returns "Hello, name" where name is the parameter
bobtest.greeting("George")

# Math is a sub-module that isn't auto-loaded.
# add() is implemented in C and adds two numbers
from bobtest import math
math.add(66,5)
```

## Build & Test the package

If you haven't already, you'll need to install python poetry.  Follow the instructions on the Poetry page.

1. Clone this repo and open a shell in this directory.
2. Bump the package version.  This is easily done via `poetry version prerelease`
3. Build the package by running `poetry build`
4. Test the package by running `poetry run pytest -s`

This will create a `dist` directory containing a tar.gz and a wheel file.

## What's in the dist directory?

Building the package creates two files, the whl file and the source tar.gz.  You can see what these files include by looking at the example_dist directory in the repo.

Both the whl and the tar.gz contain essentially the same info:
* Python source files
* Compiled C code - since I built this on my Mac, it's .so files.
* LICENSE - your license file
* METADATA - checksums of each file included in the package
* ... and so on.

# Publish the package

In order to try this out with Pypi's test environment, you'll need an API token.  Go to https://test.pypi.org and sign up, set up 2-factor, and get an API key.  Now you can configure poetry to use this repository.

```
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry config pypi-token.test-pypi <your-token>
```

Now you can publish this to PyPi's test environment

```
poetry publish -r test-pypi
```

If you're uncomfortable with the .tar.gz file being uploaded and you're going to upload for all supported platforms, you can just remove it from the dist directory before publishing.