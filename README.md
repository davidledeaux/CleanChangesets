# CleanChangesets
This script is used to delete old changesets
The use case is if a new VCS has been implemented that resets back to creating change IDs starting at 1.  Eventually the change IDs will catch up to changeset IDs already recorded in Rally and our VCS connector will no longer create changesets since it believes the work has already been done.


This script requires python 3.6 or higher and the pyral pip.


Modify the rally-v2.0.cfg file with your credentials, workspace name and a project within that workspace (this script is not project bound, however pyral requires the project)


Within the clean_changesets.py file are two variables that you will adjust.

The read_only variable is set to True by default and will only report changesets that it found to delete.

The query variable will take any WSAPI compatible query that you can use to narrow down the changesets you wish to delete.
