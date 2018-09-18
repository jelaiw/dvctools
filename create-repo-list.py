import gitlab

# Assume .python-gitlab.cfg with default.
gl = gitlab.Gitlab.from_config()
print(gl.version())

# List of group ID for 'clients', by convention, GitLab groups that are nested one level down in 'CCTS Microbiome' GitLab Group.
ccts_microbiome_client_list = list()

# See https://python-gitlab.readthedocs.io/en/stable/api-usage.html#pagination.
# Let's use the generator.
groups = gl.groups.list(as_list=False)
for g in groups:
	# Assume 'CCTS-Microbiome' GitLab Group, group ID == 129, for now.
	if g.parent_id == 129:
		ccts_microbiome_client_list.append(g.id)

# For each client, iterate over GitLab Projects, and print ssh repo url.
for gid in ccts_microbiome_client_list:
	client = gl.groups.get(gid)
	project_attrs = client.attributes['projects']

	for p in project_attrs:
		project_id = p['id']
		project = gl.projects.get(project_id)
		print(project.ssh_url_to_repo)
