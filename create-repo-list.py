import gitlab 

# Traverse the group-subgroup-project tree breadth-wise to print repo URLs.
def print_project(gid):
	group = gl.groups.get(gid)
	# Print the ssh repo URL for each project.
	project_attrs = group.attributes['projects']

	for p in project_attrs:
		project_id = p['id']
		project = gl.projects.get(project_id)
		print(project.ssh_url_to_repo)

	# Process each subgroup recursively.
	# See https://python-gitlab.readthedocs.io/en/stable/gl_objects/groups.html#subgroups for Subgroup API.
	# Also, see https://python-gitlab.readthedocs.io/en/stable/api-usage.html#pagination. Let's use the generator.
	subgroups = group.subgroups.list(as_list=False)
	for subgroup in subgroups:
		print_project(subgroup.id)

# Assume .python-gitlab.cfg is set up with default as described in "dvclib Setup" section of dvctools README. 
# See https://gitlab.rc.uab.edu/CCTS-Informatics-Pipelines/dvctools.
gl = gitlab.Gitlab.from_config()

# List of group ID for GitLab namespaces of interest.
target_gids = [ 129, 90 ]

for gid in target_gids:
	print_project(gid)
