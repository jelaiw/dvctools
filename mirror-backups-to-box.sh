#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=dvc_backup_mirror_test
#SBATCH --time=12:00:00
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=jelaiw@uab.edu

#DVC_BACKUPS_DIR=/data/scratch/jelaiw/dvc-backups

# Look at netrc for CCTS-Boxacct@uab.edu l/p.
lftp -e "lcd /data/scratch/jelaiw; mirror -R dvc-backups; bye" ftp.box.com
