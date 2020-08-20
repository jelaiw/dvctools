#!/bin/bash

VERSION=$1
DOCKER_URL=docker://$2
# Note in Singularity 3.0, instead of SIMG, we get Singularity Image File (SIF).
SIMG_FILENAME=dvctools-${VERSION}.sif
SIMG_DEPLOY_DIR=/share/apps/ngs-ccts/simg

# Load currently recommended Singularity version.
module load Singularity/3.5.2-GCC-5.4.0-2.26

# Build Singularity image.
singularity pull $DOCKER_URL

# Note in Singularity 3.0, the 'singularity pull' operation puts the SIF in current working directory (vs. SINGULARITY_CACHEDIR in previous version).
SIMG_PATH=$SIMG_FILENAME

# Set permissions to read-only.
chmod 444 $SIMG_PATH 

# Copy Singularity image to desired deploy location. 
# Note -f will overwrite existing SIMG file.
cp -f $SIMG_PATH $SIMG_DEPLOY_DIR

# Clean up. Need the -f because perms are 444.
rm -f $SIMG_PATH

# Calculate a checksum so we can tell if anything changes.
sha256sum $SIMG_DEPLOY_DIR/$SIMG_FILENAME > $SIMG_DEPLOY_DIR/${SIMG_FILENAME}.sha256sum
