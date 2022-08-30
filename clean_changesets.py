import sys
import urllib3
from pyral import Rally, rallyWorkset
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



##################################################################################

# Change this variable to False when ready to run this in non-read only mode
read_only = True

# Update this query to something that will pull the changesets that you wish to delete.  In this use case, there was an upgrade to 
# a new TFS version so the old changesets contain a URI with tfs2012 in the address.  The query can be any valid WSAPI query.
query = '(Uri CONTAINS "http://tfs2012:8080/tfs/")'

##################################################################################








options = [arg for arg in sys.argv[1:] if arg.startswith('--')]
args    = [arg for arg in sys.argv[1:] if arg not in options]
server, user, password, apikey, workspace, project = rallyWorkset(options)

print("Starting run")

rally = Rally(server, user, password, workspace=workspace, project=project, verify_ssl_cert=False)
rally.enableLogging(dest=b'rallylog.log', attrget=True)


print ("Getting changesets")
changesets = rally.get("Changeset", fetch='CommitTimestamp,Message,Name,ObjectID,Revision,Uri', query=query)

if read_only:
    print ("Running in read only mode")
else:
    print ("Running in change mode")

for changeset in changesets:
    print("Deleting {uri}".format(uri=changeset.Uri))
    if not read_only:
        rally.delete("Changeset", changeset.ObjectID)

print ("Finished run")
