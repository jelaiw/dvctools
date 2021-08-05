## Overview

`dvctools` is client-side tooling to help end users interact with our Data Version Control (DVC) implementation.

It includes Git and Git LFS client versions that have been tested together as well as various scripts to facilitate programmatic access to the GitLab API.

See `slides.pdf` for further background and context.

## End Users
### `dvclib` Setup

Perform these one-time steps to get started with `dvclib`:

1. Log in to GitLab instance at https://gitlab.rc.uab.edu/ with your blazerid.
2. Click on your avatar (at top-right in default theme) and select *Settings*.
3. Click on *Access Tokens* in sidebar (at left side of screen in default theme).
4. Create personal access token.
   * Name the token (e.g. dvclib token).
   * Make sure api checkbox in *Scopes* section is checked.
   * Click *Create personal access token* button.
5. Copy your new token to clipboard.
   * There should be a temporary field named "Your New Personal Access Token".
6. Log in to Cheaha.
7. Create `.python-gitlab.cfg` file in home directory.
   * See *python-gitlab.cfg* template for an example you can copy to your home directory and modify accordingly.
   * This template defines our GitLab instance in a `[uab]` section and sets it as default.
8. Paste access token in `private_token` field in the section that defines your GitLab instance.

*You're done!*

Next time you shell into Cheaha, when you run specific scripts, like *fork-new-project*, that call the GitLab API, you will be identified to GitLab and have the appropriate permissions.

## Developers
### Dependencies

Python source code

* Python 3
* `fork-new-project.py`
  * dvclib.gitlab
  * python-gitlab

### Tests
The recommended way to run unit tests on Cheaha (primary dev env) is to load the _dvctools_ (peg to whatever version appropriate to what you are testing) module, which will take care of the dependencies and provide an environment that should also be the exact execution environment.

See below for an example using dvctools version 1.4 and Python 3 unit test discovery (see https://docs.python.org/3/library/unittest.html#test-discovery).

```sh
[jelaiw@login001 dvctools]$ module load dvctools/1.4
[jelaiw@login001 dvctools]$ module list

Currently Loaded Modules:
  1) shared           6) binutils/2.26-GCCcore-5.4.0
  2) slurm/18.08.9    7) GCC/5.4.0-2.26
  3) rc-base          8) Go/1.13.1
  4) DefaultModules   9) Singularity/3.5.2-GCC-5.4.0-2.26
  5) GCCcore/5.4.0   10) dvctools/1.4



[jelaiw@login001 dvctools]$ singularity shell $DVCTOOLS_SIMG
Singularity> pwd
/home/jelaiw/repos/dvctools
Singularity> python3.6 --version
Python 3.6.8
Singularity> python3.6 -m unittest discover -p "*_test.py"
..........
----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
```

### Deployment
The build, test, and deploy pipeline for `dvctools` is currently implemented in GitLab CICD.

* The `build` stage builds a Docker image from Dockerfile, then pushes this image to a registry (Docker Hub).
  * Note REGISTRY_USER and REGISTRY_PASSWORD in GitLab Project Settings -> CI/CD -> Variables.
* The `test` stage runs unit tests.
* The `deploy` stage builds a Singularity image from Docker Hub, then deploys the SIMG to Cheaha.
  * Note SSH_KNOWN_HOSTS and SSH_PRIVATE_KEY in GitLab Project Settings -> CI/CD -> Variables.

See `.gitlab-ci.yml` for configuration details.

#### Other notes
Current `dvctools` release procedure:

* Update Changelog with release notes.
  * If testing, consider describing release date as *Unreleased*.
  * Otherwise, set release date accordingly.
* Increment *DVCTOOLS_VERSION* variable in `.gitlab-ci.yml`.
  * Current convention is *X.Y*, where X is major version and Y is minor version.
* Git tag.
  * Current convention is *vX.Y*, where X is major version and Y is minor version.
* Update modulefile (optional).
  * Modulefile is deployed to `/share/apps/ngs-ccts/modulefiles/dvctools`.
  * Manually copy forward existing modulefile.
  * Update *DVCTOOLS_SIMG* variable (SIF filename) in modulefile.
  * Commit updated modulefile to git repo.
  * Set default version, as appropriate. See https://lmod.readthedocs.io/en/latest/060_locating.html.
* Confirm pipeline builds, tests, and deploys in a satisfactory fashion.
