import shutil, os
from datetime import datetime, timedelta

source = '/Users/swamiprobably/Desktop/Existing_Files'
destination = '/Users/swamiprobably/Desktop/Updated_Files'

def moveUpdatedFiles():
    for files in os.listdir(source):
        #get time file was created
        created = os.path.getctime(os.path.join(source, files))
        dateCreated = datetime.fromtimestamp(created)
        
        #get time the file was modified
        modified = os.path.getmtime(os.path.join(source, files))
        dateModified = datetime.fromtimestamp(modified)
        last24hours = datetime.now() - timedelta(hours=24)
        
        #copy file created/edited within the last 24 hours
        if dateCreated > last24hours or dateModified > last24hours:
            shutil.copy(os.path.join(source, files), destination)
            

moveUpdatedFiles()
