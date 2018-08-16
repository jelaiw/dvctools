"""Functions to help us implement Data Version Control (DVC) on GitLab."""
import gitlab

def fork_new_project(gl, name, group_path, template_pid):
	"""Fork new GitLab project from template.

	Args:
		gl: gitlab.Gitlab object representing GitLab server connection.
		name: String of project name.
		group_path: String of path for target namespace.
		template_pid: Integer ID of GitLab project of template.

	Returns:
		gitlab.v4.objects.Project: The forked project.

	"""

	# Confirm we are using v4 API, the only version we are testing.
	assert gl.api_version == '4'

	# Retrieve template project by ID.
	template_project = gl.projects.get(template_pid)

	# As of GitLab version 10.8.3, GL API now expects the full namespace path.
	# So "CCTS-Microbiome/Bej-Asim", not "Bej-Asim".
	# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/68.
	# Also, see https://docs.gitlab.com/ee/api/projects.html#fork-project.
	fork = template_project.forks.create( {"namespace": group_path} )

	# Note, this is an gitlab.v4.objects.ProjectFork object.
	# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/28#note_4358.
	# We want a gitlab.v4.objects.Project object, not ProjectFork.
	forked_project = gl.projects.get(fork.id)

	# Rename project to user-specified name.
	forked_project.name = name
#	forked_project.description = "Forked from %s (project id = %s)." % (template_project.name, template_project.id)
	forked_project.description = "Forked from {0} (project id = {1}).".format(template_project.name, template_project.id) # See https://pyformat.info/.
	forked_project.save()
	# Address repo path name conflict.
	# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/29.
	forked_project.path = name
	forked_project.save()

	return forked_project
