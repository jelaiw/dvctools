## Unreleased
* Upgrade Git LFS client to version 2.8.0.
  * See https://github.com/git-lfs/git-lfs/releases/tag/v2.8.0 for list of new features, bug fixes, and documentation updates.
* Update with first pass at CICD using GitLab CICD support.
  * Add deploy job for SIMG deployment to Cheaha.

## 1.1 (2019-07-25)
* Upgrade modulefile from Singularity version 2.4.1 to 2.6.1.
  * See https://bioitx.slack.com/archives/DKYBF086Q/p1561667290002800 (Ravi, Slack, personal communication).
* Update exists\_repo() and unit test in response to GitLab 11.11 upgrade changes to git ls-remote return string.
  * See [issue #122](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/122).
* Update DVC backup contingency with ignore list.
  * See [issue #115](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/115).

## 1.0 (2019-04-22)
* Upgrade Git LFS client to version 2.7.1.
  * See https://github.com/git-lfs/git-lfs/releases/tag/v2.7.1 for list of new features, bug fixes, and documentation updates.
* Upgrade DVC backup contingency implementation.
  * Add GitLab Group watch list.
  * Refactor create repo list code for general use case (vs CCTS-Microbiome case study specific).
  * Handle empty repo and deleted repo cases.
  * See [issue #103](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/103).
* Update with first pass at CI using GitLab CICD support.
  * Add test GitLab Runner on Amazon AWS EC2.
  * See [issue #85](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/85).

### Known Issues
* `git lfs clone` of git repos greater than 2 TB in size may fail with an "Authentication required: Authorization error: Check that you have proper access to the repository" error message.
  * See [issue #116](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/116) for an example.
  * Workaround is to perform a `git lfs fetch` to retrieve the remaining LFS objects, `git lfs checkout` to check them out to your working copy, and `git lfs fsck` to double-check data integrity.
  * Possibly related to hard-coded time for GitLab git-lfs-authenticate token described at https://github.com/git-lfs/git-lfs/wiki/Limitations.

## 0.9 (2019-02-01)
* Update Dockerfile with CentOS 7.6 (1810) base image. 
  * Research Computing is updating to RHEL 7.6 for Dec 2018 Cheaha maintenance.
  * Note git is remains at version 1.8.3.1.
* Update DVC backups script with first pass at automatic repo list update.
  * See [issue #97](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/97).
* Update modulefile to Singularity bind /scratch now that /data/scratch is a symlink.
  * See [issue #100](https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/100).

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
