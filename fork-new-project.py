import gitlab

gl = gitlab.Gitlab.from_config('uab')
assert gl.api_version == '4'

prompt = "> "

print("Project name?")
project_name = input(prompt)

print("You have entered '%s'." % project_name)

print("Here is a menu of existing investigators.")

microbiome_group = gl.groups.get(129)
assert microbiome_group.name == 'CCTS-Microbiome'

groups = gl.groups.list()
clients = [ g for g in groups if g.parent_id == 129 ]

for index, client in enumerate(clients):
	print("%d.  %s" % (index, client.name))

print("Type in a number for an existing client or a name")
print("to create a new investigator subgroup in GitLab.")

client_input = input(prompt)

if client_input.isdigit(): # Proceed with an existing client.
	# Revisit to validate that client input is a legal integer.
	client = clients[int(client_input)]
	print("You have chosen an existing client: %s." % client.full_name)
else:
	print("You have chosen to create a new client: %s." % client_input)

print("Type 'yes' to proceed or Ctrl-C to quit.")
print("Proceed?")

proceed_input = input(prompt)

print(proceed_input)
