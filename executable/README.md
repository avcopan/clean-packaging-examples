# Instructions

Instructions for "building" a conda package from a static executable.

## Build for conda using rattler-build

1. `vi mess-static/recipe.yaml`
2. Copy the recipe example below into the `recipe.yaml` file
3. `rattler-build build -r mess-static`
4. To install it locally from the file, activate the desired conda environment and run `conda install /path/to/mess-static-<...>.conda`

## Publish to Anaconda.org using anaconda client

Although `rattler-build` has an upload client, it appears to have a bug, so I
am uploading using anaconda client. It can be installed as follows:
```
pixi global install anaconda-client
```
And run as follows.
```
anaconda upload -c <username> /path/to/mess-static-<...>.conda --label main
```
From there, you can install it in your conda environment as follows:
```
conda install -c <username> mess-static
```

## Recipe example

```
package:
  name: mess-static
  version: "1.2.3"

source:
  path: .

build:
  noarch: generic
  script:
    - mkdir -p ${PREFIX}/bin
    - cp ${RECIPE_DIR}/static/mess ${PREFIX}/bin/mess
    - cp ${RECIPE_DIR}/static/abstraction ${PREFIX}/bin/messabs
    - cp ${RECIPE_DIR}/static/partition_function ${PREFIX}/bin/messpf
    - cp ${RECIPE_DIR}/static/gumbo ${PREFIX}/bin/gumbo
```