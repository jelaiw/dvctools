import json
import os
import argparse

from boxsdk import JWTAuth
from boxsdk import Client

# Get Box SHA1 checksums for files that exist at and recursively below given folder.
def visit_folder(client, folder, limit, path=None):
	tuples = [] # A list of "file, checksum" tuples.

	if path is None: # Set path to root folder name.
		path = folder.name
	else:
		path = os.path.join(path, folder.name)	

	items = folder.get_items(limit)
	for item in items:
		if item.type == 'folder':
			# Add all file, checksum tuples found recursively at this folder.
			tuples.extend( visit_folder(client, client.folder(folder_id=item.id).get(), limit, path) )
		elif item.type == 'file':
			name = os.path.join(path, item.name)
			checksum = item.sha1
			# Add file, checksum tuple for this file.
			tuples.append((name, checksum)) 
		else:
			print(item)	

	return tuples

# Print (file, checksum) tuples to stdout in sha1sum -c format.
def debug_print(file_checksum_tuples):
	for file, checksum in file_checksum_tuples:
		print("{0} {1}".format(checksum, file))

def write_file(file_checksum_tuples, file_name):
	with open(file_name, 'w') as f:
		for file, checksum in file_checksum_tuples:
			f.write("{0} {1}\n".format(checksum, file))

# Parse command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument("CONFIG_FILE")
parser.add_argument("OUTPUT_FILE")
args = parser.parse_args()

# Read dvctools Box app JWT configuration from file.
with open(args.CONFIG_FILE) as f:
	config = json.load(f)

# Note Box API expects a file, so create a PEM file with hard-coded name.
pem_filename = 'private_key.pem'
with open(pem_filename, 'w') as f:
	f.write(config['boxAppSettings']['appAuth']['privateKey'])

# Create Box SDK auth and client objects.
auth = JWTAuth(
	client_id=config['boxAppSettings']['clientID'],
	client_secret=config['boxAppSettings']['clientSecret'],
	enterprise_id=config['enterpriseID'],
	jwt_key_id=config['boxAppSettings']['appAuth']['publicKeyID'],
	rsa_private_key_file_sys_path=pem_filename,
	# Note Box API expects utf-8 bytes so we call encode().
	rsa_private_key_passphrase=config['boxAppSettings']['appAuth']['passphrase'].encode(),
)
client = Client(auth)

# Clean up temporary PEM file. What is the Python equivalent of try-finally?
os.remove(pem_filename)

# Get a reference to dvc-backups folder for CCTS-Boxacct.
dvc_backups_folder = client.folder(folder_id='54010581626').get()
ITEM_LIMIT = 100
# Get SHA1 checksums from Box.
file_checksum_tuples = visit_folder(client, dvc_backups_folder, ITEM_LIMIT)
# Write SHA1 checksums to file in format that sha1sum -c expects.
write_file(file_checksum_tuples, args.OUTPUT_FILE)
