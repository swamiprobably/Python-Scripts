import shutil
import os

#shutil.copytree("/Users/swamiprobably/Desktop/Folder_A", "/Users/swamiprobably/Desktop/Folder_B/A")
#shutil.rmtree("/Users/swamiprobably/Desktop/Folder_B/A")
#shutil.copy("/Users/swamiprobably/Desktop/Folder_A/random_1.txt","/Users/swamiprobably/Desktop/Folder_B")
#os.remove("/Users/swamiprobably/Desktop/Folder_B/random_1.txt")
#shutil.move("/Users/swamiprobably/Desktop/Folder_A/","/Users/swamiprobably/Desktop/Folder_B")
'''
os.chdir("/Users/swamiprobably/Desktop/Folder_A")
#print(os.getcwd())

for f in os.listdir("/Users/swamiprobably/Desktop/Folder_A"):
    print (f)

'''
source = "/Users/swamiprobably/Desktop/Folder_A"
destination = "/Users/swamiprobably/Desktop/Folder_B"

for files in source:
    if files.endswith(".txt"):
        shutil.move(files,destination)

#print(os.getcwd())


