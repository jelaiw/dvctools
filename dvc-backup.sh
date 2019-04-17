#!/bin/bash
#SBATCH --partition=medium
#SBATCH --job-name=dvc-backup
#SBATCH --mem=16G
#SBATCH --time=24:00:00
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=jelaiw@uab.edu
#SBATCH --output=/dev/null
#SBATCH --error=/dev/null

# Location of DVC Backups directory.
DVC_BACKUPS_DIR=/data/project/bioitx/dvc-backups

# Load dependencies. 
module load dvctools/1.0

# Change dir so that relative paths in backup script work. Improve this later.
cd $DVC_BACKUPS_DIR

# Need to think about this more.
umask 077

# Get current repos from GitLab API.
singularity exec --bind /data $DVCTOOLS_SIMG python3.6 /app/create-repo-list.py < gitlab-group-watch-list.txt > tmp.txt
# Combine old repo list with current repos.
# Note this will keep the manually added repos.
# Note this also keeps old repos that are no longer in GitLab.
cat tmp.txt repo-list.txt | sort | uniq > new-repo-list.txt

# If new repo list different, replace old list with new list.
# See https://stackoverflow.com/questions/12900538/fastest-way-to-tell-if-two-files-are-the-same-in-unix-linux for a refresher on how cmp and || work.
cmp -s new-repo-list.txt repo-list.txt || { echo "Update repo list." >> $DVC_BACKUPS_DIR/backup.log; cp new-repo-list.txt repo-list.txt; }

# Clean up temporary files.
rm tmp.txt new-repo-list.txt

# Read repo-list.txt, write backups to working dir, and log to backup.log.
singularity exec --bind /data $DVCTOOLS_SIMG python3.6 /app/backup-repo.py

# Look at .netrc for CCTS-Boxacct@uab.edu l/p.
echo `date` >> $DVC_BACKUPS_DIR/backup.log # Timestamp mirror + checksum start.
echo "Mirror dvc-backups to Box FTP." >> $DVC_BACKUPS_DIR/backup.log
lftp -e "lcd $DVC_BACKUPS_DIR; lcd ..; mirror -R dvc-backups; bye" ftp.box.com

# Assume sha1sum.txt file is set up relative to dvc-backups/ in this way.
# get-box-sha1sums.py will write sha1sum.txt here.
# sha1sum -c will read sha1sum.txt, which contains relative paths.
# Clunky, but probably fine for now.
cd ..

# Box folder ID for dvc-backups dir in CCTS-Boxacct.
BOX_FOLDER_ID=54010581626 

# Get SHA1 checksums from Box dvc-backups dir in CCTS-Boxacct.
singularity exec --bind /data $DVCTOOLS_SIMG python3.6 /app/get-box-sha1sums.py ~/.657239_60ay1hpl_config.json $BOX_FOLDER_ID sha1sum.txt

# Check SHA1 checksums.
# Mismatches will be reported to standard error. See man page.
sha1sum -c sha1sum.txt > sha1sum-log.txt

# Append sha1sum -c output to backup logs. 
cat sha1sum-log.txt >> $DVC_BACKUPS_DIR/backup.log
echo "Verify SHA1 checksums from Box." >> $DVC_BACKUPS_DIR/backup.log
echo `date` >> $DVC_BACKUPS_DIR/backup.log # Timestamp mirror + checksum stop.

# Clean up.
rm sha1sum.txt sha1sum-log.txt
