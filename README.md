### Overview

dvctools is client-side tooling to help end users interact with our Data Version Control (DVC) implementation based on Git + Git LFS + GitLab + Box + Confluence.

It includes Git and Git LFS client versions that have been tested together as well as various scripts to facilitate programmatic access to the GitLab API to help us implement our vision of Data Version Control.

### Changelog

Version 0.2
* Switch to Docker/Singularity container for deployment.
* Upgrade to Git LFS client version to 2.4.0 to address [issue #55](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/55).
  * See [Git LFS 2.4.0 Changelog](https://github.com/git-lfs/git-lfs/releases/tag/v2.4.0) for full list of new features and bug fixes.

Version 0.1
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
  * There is a *python-gitlab.cfg* template at https://gitlab.rc.uab.edu/CCTS-Informatics-Pipelines/dvctools.
  * This template defines our GitLab instance in a `[uab]` section and sets it as default.
8. Paste access token in `private_token` field in the section that defines your GitLab instance.

*You're done!*

Next time you shell into Cheaha, when you run specific scripts, like *fork-new-project*, you will be identified to the GitLab API and have the appropriate permissions.