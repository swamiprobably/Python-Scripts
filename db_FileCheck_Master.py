import shutil, os, sqlite3
from tkinter import *
from tkinter import ttk
import datetime
from datetime import timedelta
from datetime import datetime


conn = sqlite3.connect('newFileDatabase.db')
c = conn.cursor()

def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS NewFileData(DATETIME NOT NULL);")

createTable()

class newFileTransfer:

    def __init__(self, master):    

        master.title('File Transfer Helper')
        master.configure(background = '#6f9de8')
        master.resizable(False, False)
       
        #label frame for description
        self.descFrame = ttk.LabelFrame(master)
        self.descFrame.grid(row=0, padx=5, pady=5, ipadx=5, ipady=5)
        self.descLabel = Label(self.descFrame, justify=LEFT, text =
                                "Copy files that have been created or modified within the last 24 hours.\n"
                                "Check the database for the timestamp of newly updated files.")
        self.descLabel.grid(row=0, padx=5, pady=5)

        #check for files to transfer 
        self.btnPrevTransfer = Button(self.descFrame, text="Check last file update date/time", command=self.checkTransfer)
        self.btnPrevTransfer.grid(row=1, column=1, padx=5, pady=5, sticky='W')
        self.entryTime = Entry(self.descFrame, width=53, state='readonly')
        self.entryTime.grid(row=1, column=0, padx=5, pady=5, sticky='E')
        
        #label frame to hold widgets
        self.labelFrame = ttk.LabelFrame(master, text="Folder Location: ")
        self.labelFrame.grid(row=1, padx=5, pady=5, ipadx=5, ipady=5)
        
        #from directory button
        self.fromLabel = Label(self.labelFrame, text="Select from:")
        self.fromLabel.grid(row=0, column=0, padx=5, pady=5, sticky='E')
        self.fromEntry = Entry(self.labelFrame, width=40, state="readonly")
        self.fromEntry.grid(row=0, column=1)
        self.btnFrom = Button(self.labelFrame, text="Choose", command=self.browseSrc)
        self.btnFrom.grid(row=0, column=2, padx=5, pady=5)

        #to directory button
        self.toLabel = Label(self.labelFrame, text="Copy to:")
        self.toLabel.grid(row=1, column=0, padx=5, pady=5, sticky='E')
        self.toEntry = Entry(self.labelFrame, width=40, state="readonly")
        self.toEntry.grid(row=1, column=1, padx=5, pady=5)
        self.btnTo = Button(self.labelFrame, text="Choose", command=self.browseDst)
        self.btnTo.grid(row=1, column=2, padx=5, pady=5) 

        #copy files button
        self.btnTransfer = Button(self.labelFrame, text="Copy Files", command=self.copyFiles)
        self.btnTransfer.grid(row=2, column=1)


    #function to check for most recent file transfer.bound to check "file/date" button
    def checkTransfer(self):
        global lastCheck, maxTime, lastCheckStr

        c.execute("SELECT MAX(DATETIME) FROM NewFileData;")
        maxTime = c.fetchone()
        if maxTime[0] is None:
            return
        else:
            lastTime = str(maxTime[0])
            lastCheck = datetime.strptime(lastTime, "%Y-%m-%d %H:%M:%S.%f")
            lastCheckStr = lastCheck.strftime("%B %d, %Y at %I:%M %p")
            self.entryTime.config(state=NORMAL)
            self.entryTime.delete(0, END)
            self.entryTime.insert(0, lastCheckStr)
            self.entryTime.config(state="readonly")

    #function browsing for the source folder bound to the "from" button
    def browseSrc(self):
        folderSrc = filedialog.askdirectory()
        self.fromEntry.config(state=NORMAL)
        self.fromEntry.delete(0, END)
        self.fromEntry.insert(0, folderSrc)
        self.fromEntry.config(state="readonly")
        
    #function browsing for the destination folder bound to the "to" button
    def browseDst(self):
        folderDst = filedialog.askdirectory()
        self.toEntry.config(state=NORMAL)
        self.toEntry.delete(0, END)
        self.toEntry.insert(0, folderDst)
        self.toEntry.config(state="readonly")

    #function to copy files to new directory and sqlite3 db. bound to "copy files" button
    def copyFiles(self):
        src = self.fromEntry.get()
        dst = self.toEntry.get()
        
        currentTime = datetime.now()
        previousTime = (currentTime) - (timedelta(hours = 24))

        for fileName in os.listdir(src):
            path = os.path.join(src, fileName)
            modStat = os.stat(path).st_mtime
            modTime = datetime.fromtimestamp(modStat)
            shutil.copy2(path, dst)
        
        #update database
        current = datetime.now()
        now = str(current)
        sql_insert = "INSERT INTO NewFileData VALUES('{}');".format(now)
        c.execute(sql_insert)
        conn.commit()
        newFileData = current.strftime("%B %d, %Y  %I:%M %p")
        self.entryTime.insert(0, newFileData)

        
def main():
    root = Tk()
    my_gui = newFileTransfer(root)
    root.mainloop()

if __name__ == "__main__": main()

