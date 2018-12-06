#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=dvc-sha1sum
#SBATCH --mem=4G
#SBATCH --time=12:00:00
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=jelaiw@uab.edu
##SBATCH --output=/dev/null
##SBATCH --error=/dev/null

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
module load dvctools/0.8

# Change dir so that relative paths in backup script work. Improve this later.
cd $DVC_BACKUPS_DIR
# Assumes sha1sum.txt file is set up relative to dvc-backups/ in this way.
cd ..
CWD=$(pwd)
# Get SHA1 checksums from Box dvc-backups dir in CCTS-Boxacct.
singularity exec --bind /data $DVCTOOLS_SIMG python3.6 /app/get-box-sha1sums.py ~/.657239_60ay1hpl_config.json 54010581626 $CWD/sha1sum.txt
# Check SHA1 checksums.
# Mismatches will be reported to standard error. See man page.
sha1sum -c sha1sum.txt
# Clean up.
rm sha1sum.txt
