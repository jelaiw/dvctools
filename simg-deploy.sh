#!/bin/bash

# See https://stackoverflow.com/questions/192319/how-do-i-know-the-script-file-name-in-a-bash-script.
if [[ $# -eq 0 ]]; then
	echo "Usage: ${0##*/} <PATH TO SIMG TO DEPLOY>"
	exit 1
fi

SIMG_PATH=$1
SIMG_NAME=`basename $SIMG_PATH`
SIMG_DIR=/share/apps/ngs-ccts/simg

# Copy Singularity container to deploy location. 
# Note -f will overwrite existing SIMG file.
cp -f $SIMG_PATH $SIMG_DIR
# Calculate a checksum so we can tell if anything changes.
sha256sum $SIMG_DIR/$SIMG_NAME > $SIMG_DIR/${SIMG_NAME}.sha256sum
# Remove SIMG from staging location.
rm -f $SIMG_PATH
