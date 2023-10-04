from pytube import YouTube
from tkinter import *
from tkinter import ttk
from icecream import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

def video_downloader():
    video_url = link.get()
    # passing the url to the YouTube object
    global progressbar
    progressbar = ttk.Progressbar(frm, orient="horizontal",length=50, mode='determinate')
    progressbar.grid(column=0, row=4, sticky="nsew")
    global pPercentage
    pPercentage = ttk.Label(frm, text="")
    pPercentage.grid(column=1, row=4, sticky="nsew")

    my_video = YouTube(video_url,on_progress_callback=progress_function)
    # my_video = YouTube(video_url)

    # downloading the video in high resolution
    my_video.streams.get_highest_resolution().download("./Downloads")
    
    conclude_download(my_video)
    #concluido
    
def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pcompletion = bytes_downloaded /total_size*100
    per = str(int(pcompletion))
    
    
    pPercentage.configure(text=per+ '%')
    pPercentage.update()


    progressbar.configure(value=float(pcompletion))
    progressbar.update()

def conclude_download(my_video):
    ttk.Label(frm, text=f'"{my_video.title}" foi baixado!', width=100).grid(column=0, row=4, columnspan=2, sticky="nsew")
    response = requests.get(my_video.thumbnail_url)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    panel = ttk.Label(frm,image=img)
    panel.grid(column=0, row=5, columnspan=2, sticky="nsew")
    panel.image = img # escapa do python garbage collector

# def progress_function(self, stream, chunk,file_handle, bytes_remaining):

#     size = self.video.filesize
#     progress = (float(abs(bytes_remaining-size)/size))*float(100))
#     self.loadbar.setValue(progress)

# def percent(tem, total):
#         perc = (float(tem) / float(total)) * float(100)
#         return perc


root = Tk() # main windows
root.geometry('640x700')
root.resizable(width=False,height=False)
root.title("Youtube Downloader")
img = ImageTk.PhotoImage(file='./assets/youtube.png')
root.iconphoto(True,img)

frm = ttk.Frame(root, height=100, width=120) # cria o frame
frm.grid() # cria o grid

ttk.Label(frm, text="Bem-vindo ao Youtube Downloader do Augusto!").grid(column=0, row=0, columnspan=2)
ttk.Label(frm, text="Insira o Link para baixar o seu vídeo:").grid(column=0, row=1, sticky="w")

link = ttk.Entry(frm, width=70)
link.grid(column=1,row=1, sticky="w")

ttk.Button(frm, text="Baixar", command=video_downloader, width=80).grid(column=0, row=2, columnspan=2, sticky="w")
ttk.Button(frm, text="Sair", command=root.destroy, width=80).grid(column=0, row=3, columnspan=2, sticky="w")
root.mainloop()