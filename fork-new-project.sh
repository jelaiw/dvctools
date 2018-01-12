#!/bin/sh

QWRAP_SUPPORT_SCRIPTS_HOME=/share/apps/ngs-ccts/QWRAP-support-scripts

# Load the specific Python3 version we have been testing.
module load Python/3.6.3-intel-2017a

# Load the python-gitlab venv.
. $QWRAP_SUPPORT_SCRIPTS_HOME/python-gitlab-venv/bin/activate

# Run fork-new-project.py.
python3 fork-new-project.py "$@"

# Clean up. Deactivate python-gitlab venv and unload Python3 module.
deactivate
module unload Python/3.6.3-intel-2017a
