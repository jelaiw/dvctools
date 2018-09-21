FROM centos:7.4.1708

MAINTAINER jelaiw@uab.edu

# Install wget (for grabbing git-lfs client release).
# Install man (for access to git man pages).
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_9603.
RUN yum -y install man-db wget

# Install Git 1.8.3.1 and Git LFS client version 2.5.1.
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_9605.
RUN yum -y install --setopt=tsflags='' git && \
	cd /tmp && \
	wget https://github.com/git-lfs/git-lfs/releases/download/v2.5.1/git-lfs-linux-amd64-v2.5.1.tar.gz && \
	tar zxvf git-lfs-linux-amd64-v2.5.1.tar.gz && \
	./install.sh

# Install Python 3.6, python-gitlab 1.5.1, and dvclib.

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
	yum -y install python36u python36u-pip

RUN pip3.6 install python-gitlab

ENV APPROOT="/app"

WORKDIR $APPROOT

COPY fork-new-project.py $APPROOT
COPY dvclib $APPROOT/dvclib
COPY backup-repo.py $APPROOT

ENTRYPOINT ["/bin/bash"]
