#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=dvc_backup_mirror_test
#SBATCH --time=12:00:00
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=jelaiw@uab.edu
#SBATCH --output=/dev/null
#SBATCH --error=/dev/null

DVC_BACKUPS_DIR=/data/scratch/jelaiw/dvc-backups

# Look at netrc for CCTS-Boxacct@uab.edu l/p.
echo -n "Mirroring dvc-backups to Box FTP ... " >> $DVC_BACKUPS_DIR/backup.log
lftp -e "lcd /data/scratch/jelaiw; mirror -R dvc-backups; bye" ftp.box.com
echo "done." >> $DVC_BACKUPS_DIR/backup.log
