import argparse
import gitlab
from dvclib import fork_new_project

# Set up argument parser.
parser = argparse.ArgumentParser(description="Fork new GitLab project from a template to given client namespace.")
parser.add_argument(
	"PROJECT_NAME", help="Name for newly forked GitLab project.")
parser.add_argument(
	"CLIENT_NAME", help="Name of client. Example: Bej-Asim")
args = parser.parse_args()

# Log debug so caller can confirm input parameters.
print("PROJECT_NAME = %s" % args.PROJECT_NAME)
print("CLIENT_NAME = %s" % args.CLIENT_NAME)

# Create GitLab server connection from config profile.
gl = gitlab.Gitlab.from_config('uab')

# dvclib.fork_new_project() does the heavy lifting.
forked_project = fork_new_project(gl, args.PROJECT_NAME, args.CLIENT_NAME)

# Print SSH URL to new repo.
# You would otherwise have to go to the repo browser to get this.
print("git clone %s" % forked_project.ssh_url_to_repo)
