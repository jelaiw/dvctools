FROM centos:7.8.2003

MAINTAINER jelaiw@uab.edu

# Install wget (for grabbing git-lfs client release).
# Install man (for access to git man pages).
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_9603.
# Install EPEL release package to get at 7zip in EPEL.
# Install Python 3.
RUN yum -y install man-db wget epel-release python3

# Install p7zip (for 7za call in backup repo script).
RUN yum -y install p7zip

# Install Git 1.8.3.1 and Git LFS client version 2.10.0.
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_9605.
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/86#note_10453.
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/116#note_13558.
RUN yum -y install --setopt=tsflags='' git && \
	cd /tmp && \
	wget https://github.com/git-lfs/git-lfs/releases/download/v2.10.0/git-lfs-linux-amd64-v2.10.0.tar.gz && \
	tar zxvf git-lfs-linux-amd64-v2.10.0.tar.gz && \
	./install.sh

# Install python-gitlab 1.5.1 and Box Python SDK 1.5 + JWT.
# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/140 for research on pip read timeouts.
RUN pip3 install --retries 9 --timeout 99 "python-gitlab==1.5.1" "boxsdk>=1.5,<2.0[jwt]"

ENV APPROOT="/app"

WORKDIR $APPROOT

COPY fork-new-project.py $APPROOT
COPY dvclib $APPROOT/dvclib
COPY backup-repo.py $APPROOT
COPY create-repo-list.py $APPROOT

# See https://gitlab.com/gitlab-org/gitlab-runner/issues/2109.
ENTRYPOINT ["/bin/bash", "-l", "-c"]
