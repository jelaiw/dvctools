#!/bin/sh

# Relative locations of GitLab API support scripts and python-gitlab venv.
GITLAB_API_SUPPORT_SCRIPTS_HOME=/share/apps/ngs-ccts/gitlab-api-support-scripts
PYTHON_GITLAB_VENV_HOME=$GITLAB_API_SUPPORT_SCRIPTS_HOME/python-gitlab-venv

# Load the specific Python3 version we have been testing.
module load Python/3.6.3-intel-2017a

# Load the python-gitlab venv.
. $PYTHON_GITLAB_VENV_HOME/bin/activate

# Run fork-new-project.py. Note production symlink.
python3 $GITLAB_API_SUPPORT_SCRIPTS_HOME/production/fork-new-project.py "$@"

# Clean up. Deactivate python-gitlab venv and unload Python3 module.
deactivate
module unload Python/3.6.3-intel-2017a
