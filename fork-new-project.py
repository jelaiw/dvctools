import argparse
import gitlab
from dvclib import fork_new_project

# Set up argument parser.
parser = argparse.ArgumentParser(description="Fork new GitLab project from a template to given namespace.")
parser.add_argument(
	"PROJECT_NAME", help="Name for newly forked GitLab project.")
parser.add_argument(
	"GROUP_PATH", help="Path to desired GitLab Group namespace. Example: CCTS-Microbiome/Bej-Asim")
parser.add_argument(
	"TEMPLATE_PID", help="GitLab project ID of template. Example: 220")
args = parser.parse_args()

# Log debug so caller can confirm input parameters.
print("PROJECT_NAME = %s" % args.PROJECT_NAME)
print("GROUP_PATH = %s" % args.GROUP_PATH)
print("TEMPLATE_PID = %s" % args.TEMPLATE_PID)

# Create GitLab server connection from config profile.
gl = gitlab.Gitlab.from_config('uab')

# dvclib.fork_new_project() does the heavy lifting.
forked_project = fork_new_project(gl, args.PROJECT_NAME, args.GROUP_PATH, args.TEMPLATE_PID)

# Print SSH URL to new repo.
# You would otherwise have to go to the repo browser to get this.
print("ssh repo url = %s" % forked_project.ssh_url_to_repo)
