### Overview

dvctools is client-side tooling to help end users interact with our Data Version Control (DVC) implementation based on Git + Git LFS + GitLab + Box + Confluence.

It includes Git and Git LFS client versions that have been tested together as well as various scripts to facilitate programmatic access to the GitLab API to help us implement our vision of Data Version Control.

### Changelog

__Version 0.5__
* Install man and man pages for git.
  * See [issue #81 note](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_9603).

__Version 0.4__
* Update to address `git init` problem with a missing Singularity bind point.
  * See [issue #82](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/82).
  * A big TY to Curtis for reporting!!

__Version 0.3__
* Update `dvc-fork -h` help text with up-to-date example for "group path" (i.e. full path to GitLab Group namespace).
  * See [issue #68](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/68).
* Upgrade python-gitlab version to 1.5.1.
  * See [python-gitlab release notes](http://python-gitlab.readthedocs.io/en/stable/release_notes.html).
* Upgrade Git LFS client version to 2.5.1.
  * See [Git LFS changelog](https://github.com/git-lfs/git-lfs/releases) for details about new features and bug fixes between version 2.4.0 and 2.5.1.

__Version 0.2__
* Switch to Docker/Singularity container + modulefile for deployment on Cheaha.
* Upgrade Git LFS client version to 2.4.0 to address [issue #55](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/55).
  * See [Git LFS 2.4.0 Changelog](https://github.com/git-lfs/git-lfs/releases/tag/v2.4.0) for full list of new features and bug fixes.

__Version 0.1__
* Upgrade Git LFS client version to 2.3.4 to address [issue #25](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/25).

### dvclib Setup

Perform these optional one-time steps to get started with dvclib:

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
7. Create `.python-gitlab.cfg` file.
  * See *python-gitlab.cfg* template for an example you can copy to your home directory and modify accordingly.
  * This template defines our GitLab instance in a `[uab]` section and sets it as default.
8. Paste access token in `private_token` field in the section that defines your GitLab instance.

*You're done!*

Next time you shell into Cheaha, when you run specific scripts, like *fork-new-project*, you will be identified to the GitLab API and have the appropriate permissions.
