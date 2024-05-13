# Steps
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