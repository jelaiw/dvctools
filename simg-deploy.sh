#!/bin/bash

VERSION=1.2
DOCKER_URL=docker://jelaiw/dvctools:$VERSION
SIMG_FILENAME=dvctools-$VERSION.simg
SIMG_DEPLOY_DIR=/share/apps/ngs-ccts/simg

# Load currently recommended Singularity version.
module load Singularity/2.6.1-GCC-5.4.0-2.26

# Build Singularity image.
singularity pull $DOCKER_URL

# Set permissions to read-only.
chmod 444 $SIMG_FILENAME 

# Copy Singularity image to desired deploy location. 
# Note -f will overwrite existing SIMG file.
cp -f $SIMG_FILENAME $SIMG_DEPLOY_DIR

# Clean up. Need the -f because perms are 444.
rm -f $SIMG_FILENAME

# Calculate a checksum so we can tell if anything changes.
sha256sum $SIMG_DEPLOY_DIR/$SIMG_FILENAME > $SIMG_DEPLOY_DIR/${SIMG_FILENAME}.sha256sum
