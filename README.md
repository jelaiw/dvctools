### Overview

These support scripts make use of *python-gitlab* to facilitate programmatic access to the GitLab API to help us implement Data Version Control.

### Setup

Perform these one-time steps to get started:

1. Log in to GitLab instance at https://gitlab.rc.uab.edu/ with your blazerid.
2. Click on your avatar (at top-right in default theme) and select *Settings*.
3. Click on *Access Tokens* in sidebar (at left side of screen in default theme).
4. Create personal access token.
  * Name the token (e.g. gitlab-api-support-scripts token).
  * Make sure api checkbox in *Scopes* section is checked.
  * Click *Create personal access token* button.
5. Copy your new token to clipboard.
  * There should be a temporary field named "Your New Personal Access Token".
6. Log in to Cheaha.
7. Create `.python-gitlab.cfg` file.
  * There is a *python-gitlab.cfg* template at https://gitlab.rc.uab.edu/CCTS-Informatics-Pipelines/gitlab-api-support-scripts.
  * This template defines our GitLab instance in a `[uab]` section and sets it as default.
8. Paste access token in `private_token` field in the section that defines your GitLab instance.
9. Make sure production installation on Cheaha is defined in your PATH.
  * Location is `/share/apps/ngs-ccts/gitlab-api-support-scripts/production`.
  * I suggest defining a `GITLAB_API_SUPPORT_SCRIPTS_HOME` variable in your `.bashrc` file and making sure it is part of your `PATH`.

*You're done!*

Next time you shell into Cheaha, the production deployment of these support scripts will be in your path, and when you run specific scripts, like *fork-new-project*, you will be identified to the GitLab API and have the appropriate permissions.