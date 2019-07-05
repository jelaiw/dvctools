#!/bin/bash
VERSION=1.1
SIMG_NAME=dvctools-$VERSION.simg

# Build Docker image.
docker build -t jelaiw/dvctools:$VERSION .
# Make sure Docker image exists at Docker Hub.
docker push jelaiw/dvctools:$VERSION
# Build Singularity container.
sudo singularity build $SIMG_NAME docker://jelaiw/dvctools:$VERSION
# Fix the owner and permissions.
sudo chown ec2-user:ec2-user $SIMG_NAME 
chmod 444 $SIMG_NAME 
# Copy to Cheaha. Note this goes directly to my home directory.
scp $SIMG_NAME jelaiw@cheaha.rc.uab.edu:~
# Clean up. Need the -f because perms are 444.
rm -f $SIMG_NAME
