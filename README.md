### Overview

dvctools is client-side tooling to help end users interact with our Data Version Control (DVC) implementation based on Git + Git LFS + GitLab + Box + Confluence.

It includes Git and Git LFS client versions that have been tested together as well as various scripts to facilitate programmatic access to the GitLab API to help us implement our vision of Data Version Control.

### dvclib Setup

Perform these one-time steps to get started with dvclib:

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

Next time you shell into Cheaha, when you run specific scripts, like *fork-new-project*, that call the GitLab API, you will be identified to GitLab and have the appropriate permissions.
