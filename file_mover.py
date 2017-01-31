import shutil
import os


source = '/Users/swamiprobably/Desktop/Folder_A'
destination = '/Users/swamiprobably/Desktop/Folder_B'

for files in os.listdir(source):                #Loop through dir
    if files.endswith('.txt')                   #Find all .txt files
        path = os.path.join(source, files)      #Save file path
        print('File path: {}').format(path)     #Print path for moved file
        shutil.move(path, destination)          #Move file to new destination
    
