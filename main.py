from tkinter import ttk
from tkinter import *
from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
font=('verdana',20)
file_size=0


def completeDownload(stream=None, file_path=None):
    print("Download completed")
    showinfo("Message", "File has been downloaded...")
    dbtn['text']="Download video"
    dbtn['state']="active"
    urlField.delete(0,END)
    youtubeChoices.delete(0,END)

def progressDownload(stream=None, chunk=None, bytes_remainig=None):
    percent=((file_size -bytes_remainig)/file_size)*100
    dbtn['text']="{:00.0f}%downloaded".format(percent)

def startDownload(url):
    global file_size
    choice = youtubeChoices.get()
    video = urlField.get()
    path_to_save=askdirectory()
    if path_to_save is None:
        return

    try:

        yt = YouTube(url)




        if (len(video) > 1):
            urlField.config(text="")
            print(video, "at", path_to_save)
            yt = YouTube(video, on_progress_callback=progressDownload)
            print("video name is:\n\n", yt.title)
            if (choice == downloadChoices[0]):
                print("720p video is downloading....")
                st = yt.streams.first()



            elif (choice == downloadChoices[1]):
                print("Audio file is downloading...")
                st = yt.streams.last()
        else:
            print("rajat")




        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)

        file_size=st.filesize
        st.download(output_path=path_to_save)




    except Exception as e:
        print(e),
        print("error !!")

def btnclicked():
    try:
        dbtn['text']= "Please wait..."
        dbtn['state']='disabled'
        url=urlField.get()
        if url=='':
            return
        print(url)
        thread=Thread(target=startDownload,args=(url,))
        thread.start()

    except Exception as e:
        print(e)


def startDownloadThread():
    thread=Thread(target=startDownload)
    thread.start()





main=Tk()
main.title("My Youtube Downloader")


main.iconbitmap('Graphics-Vibe-Shield-Badge-Social-Youtube.ico')
main.geometry("500x600")



file=PhotoImage(file='youtube_button.png')

headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP,pady=5)


youtubeLinkLabel=Label(main,text="Enter youtube link here..",
                       fg="blue",font=("Agency FB",30))
youtubeLinkLabel.pack(side=TOP,pady=15)


urlField=Entry(main,font=("verdana",20),justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=20,pady=15)
urlField.focus()

youtubeChooseLabel=Label(main,text="Please choose what to download:",fg="blue",
                         font=("Agency FB", 20 ))
youtubeChooseLabel.pack(side=TOP,pady=5)
downloadChoices =["Mp4 720p",
                  "Song Mp3"]

youtubeChoices = ttk.Combobox(main,values= downloadChoices)
youtubeChoices.pack(side=TOP,pady=5)




dbtn=Button(main,text="Download ",font=("verdana",20),relief='ridge',command=btnclicked)
dbtn.pack(side=TOP,pady=40)

loadingLabel = ttk.Label(main,text="App developed by |>RAJAT",
                         font=("Agency FB", 20) )
loadingLabel.pack(side=TOP,pady=70)

main.mainloop()

