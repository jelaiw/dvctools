import argparse
import gitlab
from dvclib import fork_new_project

parser = argparse.ArgumentParser(description="Fork new GitLab project from a template to given client namespace.")
parser.add_argument(
	"PROJECT_NAME", help="Name for newly forked GitLab project.")
parser.add_argument(
	"CLIENT_NAME", help="Name of client. Example: Bej-Asim")
args = parser.parse_args()

print("PROJECT_NAME = %s" % args.PROJECT_NAME)
print("CLIENT_NAME = %s" % args.CLIENT_NAME)

# Create GitLab server connection from config profile.
gl = gitlab.Gitlab.from_config('uab')

forked_project = fork_new_project(gl, args.PROJECT_NAME, args.CLIENT_NAME)

print("git clone %s" % forked_project.ssh_url_to_repo)
