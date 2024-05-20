# Instructions

Instructions for building a simple, pure-python package.

## Set-up

1. `poetry new test-package-<username>`
2. Add a `hello()` function to the `__init__.py` that prints "Hello, world!"

## Local Installation (for Development)

1. `cd test-package-<username>`
2. `pip install -e .`

## Publish to PyPI (using TestPyPI for practice)

1. `cd test-package-<username>`
2. `poetry build`
3. `poetry publish -r test-pypi`
    - For TestPyPI, create account on TestPyPI with an API token and configure as follows:
        - `poetry config repositories.test-pypi https://test.pypi.org/legacy/`
        - `poetry config pypi-token.test-pypi <your-token>`

## Build for conda using rattler-build

1. `vi test-package-<username>/recipe.yaml`
2. Copy the recipe example below into the `recipe.yaml` file
3. `rattler-build build -r test-package-<username>`
4. To install it locally from the file, activate the desired conda environment and run `conda install /path/to/test-package-<username...>.conda`

## Publish to Anaconda.org

If you have an API token for anaconda.org, you can publish the package
there as follows:
```
export ANACONDA_API_KEY=<API token>
rattler-build upload anaconda -o <username> /path/to/test-package-<username...>.conda
```
Note: If using the `-c` flag, be aware that it specifies the *label* (e.g. 'main'), not the conda channel.

## Testing

You can test it out in a conda environment as follows:
```
mamba create -n packaging python=3
conda activate packaging
pip install -i https://test.pypi.org/simple/ test-package-<username>
python
>>> import test_package_<username>
>>> test_package_<username>.hello()
```
This should print "Hello, world!" to the screen.


## Recipe example

```
package:
  name: test-package-<username>
  version: "1.2.3"

source:
  path: .

build:
  noarch: python 
  script: pip install . -v

requirements:
  host:
    - pip
    - python >=3.9
    - poetry
    - wheel
  run:
    - python >=3.9
```