import shutil, os
import datetime
from tkinter import *
from tkinter import ttk

class fileTransfer:

    def __init__(self, master):    

        master.title('File Transfer Helper')
        master.configure(background = '#6f9de8')
        master.resizable(False, False)
       
        #label frame for instructions
        self.descFrame = ttk.LabelFrame(master)
        self.descFrame.grid(row=0, padx=10, pady=10, ipadx=10, ipady=10)
        self.descLabel = Label(self.descFrame, wraplength = 500, justify=LEFT, text =
                                "Copy files that have been created or modified within the last 24 hours.")
        self.descLabel.grid(row=0, column=0, padx=5, pady=5)

        
        #label frame to hold all widgets
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

        #transfer button
        self.btnTransfer = Button(self.labelFrame, text="TRANSFER", command=self.start_transfer)
        self.btnTransfer.grid(row=2, column=1)


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

    #function for starting the file transfer bound to the "transfer" button
    def start_transfer(self):
        src = self.fromEntry.get()
        dst = self.toEntry.get()
        
        currentTime = datetime.datetime.now()
        previousTime = (currentTime) - (datetime.timedelta(hours = 24))

        for fileName in os.listdir(src):
            path = os.path.join(src, fileName)
            modStat = os.stat(path).st_mtime
            modTime = datetime.datetime.fromtimestamp(modStat)
            shutil.copy2(path, dst)






def main():            
    
    root = Tk()
    my_gui = fileTransfer(root)
    root.mainloop()
    
if __name__ == "__main__": main()
