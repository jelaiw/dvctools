#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=dvc_backup_test
#SBATCH --mem=4096
#SBATCH --time=12:00:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=jelaiw@uab.edu

# Location of DVC Backups directory.
DVC_BACKUPS_DIR=/data/scratch/jelaiw/dvc-backups
# Location of backup-repo python script.
DVCTOOLS_DIR=~/repos/dvctools

# Load dependencies. Modules for now. Container later.
module load Python/3.6.3-intel-2017a Singularity/2.4.1-GCC-5.4.0-2.26

# Change dir so that relative paths in backup script work. Fix this later.
cd $DVC_BACKUPS_DIR
# Call backup script, which reads repo-list.txt, and logs to backup.log.
python $DVCTOOLS_DIR/backup-repo.py
