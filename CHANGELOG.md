## 0.9 (Unreleased)
* Update Dockerfile with CentOS 7.6 (1810) base image. 
  * Research Computing is updating to RHEL 7.6 for Dec 2018 Cheaha maintenance.
  * Note git is remains at version 1.8.3.1.
* Update DVC backups script with first pass at automatic repo list update.
  * See [issue #97](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/97).

## 0.8 (2018-12-07)
* Upgrade Git LFS client to version 2.6.1.
  * See https://github.com/git-lfs/git-lfs/releases/tag/v2.6.1 for release notes.
* Upgrade to retrieve SHA1 checksums from Box API and check them against latest DVC backups as part of the nightly backup process.
  * Include Box Python 1.5 SDK + JWT support.
  * See [issue #92](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/92).

## 0.7 (2018-11-30)
* Upgrade Git LFS client to version 2.6.0.
  * See https://github.com/git-lfs/git-lfs/releases/tag/v2.6.0 for release notes.
* Rewrite modulefile aliases as functions to support both non-interactive and interactive calls to "git" and "dvc-fork".
  * See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/94. 
  * A big TY to Liam for reporting.
* Update SLURM backup job script to request 16 GB of RAM.
  * See [issue #96 note](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/96#note_10963).

## 0.6 (2018-10-19)
* Update backup repo script with 7za volumes to address Box 15 GB limit.
  * See [issue #84](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/84).
* Upgrade backup repo SLURM job script to run in cron.
* Add DVCTOOLS\_SIMG environment variable to modulefile.

## 0.5 (2018-09-24)
* Install man and man pages for git.
  * See [issue #81 note](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/81#note_9603).
* Install 7zip to Docker image in support of backup repo script.

## 0.4 (2018-09-18)
* Update to address `git init` problem with a missing Singularity bind point.
  * See [issue #82](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/82).
  * A big TY to Curtis for reporting!!

## 0.3 (2018-08-13)
* Update `dvc-fork -h` help text with up-to-date example for "group path" (i.e. full path to GitLab Group namespace).
  * See [issue #68](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/68).
* Upgrade python-gitlab version to 1.5.1.
  * See [python-gitlab release notes](http://python-gitlab.readthedocs.io/en/stable/release_notes.html).
* Upgrade Git LFS client version to 2.5.1.
  * See [Git LFS changelog](https://github.com/git-lfs/git-lfs/releases) for details about new features and bug fixes between version 2.4.0 and 2.5.1.

## 0.2 (2018-06-01)
* Switch to Docker/Singularity container + modulefile for deployment on Cheaha.
* Upgrade Git LFS client version to 2.4.0 to address [issue #55](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/55).
  * See [Git LFS 2.4.0 Changelog](https://github.com/git-lfs/git-lfs/releases/tag/v2.4.0) for full list of new features and bug fixes.

## 0.1 (2018-05-02)
* Upgrade Git LFS client version to 2.3.4 to address [issue #25](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/25).
