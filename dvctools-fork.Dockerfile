FROM centos:7.4.1708

MAINTAINER jelaiw@uab.edu

# Install Git 1.8.3.1 and Git LFS client version 2.4.0.

RUN yum -y install git wget && \
	cd /tmp && \
	wget https://github.com/git-lfs/git-lfs/releases/download/v2.4.0/git-lfs-linux-amd64-2.4.0.tar.gz && \
	tar zxvf git-lfs-linux-amd64-2.4.0.tar.gz && \
	cd git-lfs-2.4.0 && \
	./install.sh

# Install Python 3.6, python-gitlab 1.3.0, and dvclib.

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
	yum -y install python36u python36u-pip

RUN pip3.6 install python-gitlab

ENV APPROOT="/app"

WORKDIR $APPROOT

COPY fork-new-project.py $APPROOT
COPY dvclib.py $APPROOT

ENTRYPOINT ["python3.6", "/app/fork-new-project.py"]
