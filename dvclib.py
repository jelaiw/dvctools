import gitlab

def fork_new_project(name, namespace, template_pid=220):
	"""Fork new GitLab project from template project."""

	gl = gitlab.Gitlab.from_config('uab')
	assert gl.api_version == '4'

	# Retrieve template project by ID.
	template_project = gl.projects.get(template_pid)

	# This is an gitlab.v4.objects.ProjectFork object.
	# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/28#note_4358.
	fork = template_project.forks.create( {"namespace": namespace} )
	# We want gitlab.v4.objects.Project.
	forked_project = gl.projects.get(fork.id)

	forked_project.name = name
	forked_project.description = "Forked from QWRAP production template."
	forked_project.save()
	# Address repo path name conflict.
	# See https://gitlab.rc.uab.edu/jelaiw/ccts-bmi-incubator/issues/29.
	forked_project.path = name
	forked_project.save()

#fork_new_project("M142", "Bej-Asim")
