from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0

# this gets called for updating percentage
def progress(stream=None, chunk=None, file_handle=None, remaining=None):
    # gets the percentage of file that is been downloaded
    file_downloaded = (file_size - remaining)
    per = (file_downloaded/file_size)*100
    DBtn.config(text =" {:00.of} % downloaded".format(per))

def StartDownload():
    global file_size
    try:
        url=urlField.get()
        DBtn.config(text="Please wait...")
        DBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        # creating youtube object with url
        ob = YouTube(url)
        # YouTube(on_progress_callback=progress)
        strms = ob.streams.filter(res="720p",type="video").first()
        file_size = strms.filesize
        vTitle.config(text=strms.title)
        vTitle.pack(side=TOP)
        print(strms)
        strms.download(output_path=path_to_save_video)
        print("done....")
        DBtn.config(text="Start Download")
        DBtn.config(state=NORMAL)
        showinfo("Donwload finished","Download successfully")
        urlField.delete(0,END)
        vTitle.pack_forget()


    except Exception as e:
        print(e)
        print("Error !!")
        DBtn.config(text="Error")

def StartDownloadthread():
    #   creating thread
    thread = Thread(target=StartDownload)
    thread.start()

# starting GUI building

main = Tk()

main.title("YouTube Downloader")

# setting icon

main.iconbitmap('E:\jibran\PYTHON  projects\Youtube-downloader\icon.ico')

main.geometry("500x600")

# heading icon
file=PhotoImage(file='E:\jibran\PYTHON  projects\Youtube-downloader\icon.png')
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP)

# url text field
urlField = Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=30)

# downlaod button 

DBtn = Button(main,text="Start download",font=("verdana",18),relief='ridge',command=StartDownloadthread)
DBtn.pack(side=BOTTOM,pady=45)

# video title
vTitle = Label(main,text="Title",font=(18))


main.mainloop()

