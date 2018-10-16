#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=dvc_backup_test
#SBATCH --mem=4096
#SBATCH --time=12:00:00
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=jelaiw@uab.edu

# Build env that cron needs.
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_9724.
module ()
{
	eval `/cm/local/apps/environment-modules/3.2.10/Modules/3.2.10/bin/modulecmd bash $*`
}

# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_9725.
export MODULEPATH=/share/apps/rc/modules/all:/share/apps/ngs-ccts/modulefiles

# Location of DVC Backups directory.
DVC_BACKUPS_DIR=/data/scratch/jelaiw/dvc-backups

# Load dependencies. 
module load dvctools/0.6

# Change dir so that relative paths in backup script work. Improve this later.
cd $DVC_BACKUPS_DIR
# Call backup script, which reads repo-list.txt, and logs to backup.log.
singularity exec --bind /data $DVCTOOLS_SIMG python3.6 /app/backup-repo.py
