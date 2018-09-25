#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=dvc_backup_test
#SBATCH --mem=4096
#SBATCH --time=12:00:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=jelaiw@uab.edu

# Location of DVC Backups directory.
DVC_BACKUPS_DIR=/data/scratch/jelaiw/dvc-backups

# Load dependencies. 
module load dvctools/0.5

# Change dir so that relative paths in backup script work. Improve this later.
cd $DVC_BACKUPS_DIR
# Call backup script, which reads repo-list.txt, and logs to backup.log.
singularity exec --bind /data $DVCTOOLS_SIMG python3.6 /app/backup-repo.py
