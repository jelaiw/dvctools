FROM centos:7.4.1708

MAINTAINER jelaiw@uab.edu

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
	yum -y install python36u python36u-pip

RUN pip3.6 install python-gitlab

ENV APPROOT="/app"

WORKDIR $APPROOT

COPY fork-new-project.py $APPROOT
COPY dvclib.py $APPROOT

ENTRYPOINT ["python3.6", "$APPROOT/fork-new-project.py"]
