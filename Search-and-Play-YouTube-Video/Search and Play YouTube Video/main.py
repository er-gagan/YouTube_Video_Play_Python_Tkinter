from tkinter import *
from YouTube import *
from bs4 import BeautifulSoup as soup
import urllib.parse
from PIL import Image, ImageTk
import io,os
from tkinter.messagebox import *

root = Tk()
root.geometry('1000x580')

photo = PhotoImage(file="./logo.png")
root.iconphoto(False,photo)

root.title("YouTube Play Music")

image1 = PhotoImage(file="./banner.png")
label_for_image = Label(root,image=image1)
label_for_image.place(x=170, y=-1)

SearchVar = StringVar()
os.system("cls")

def Search():
    def PlayAudio(vidlink,title,duration):
        audio_root = Toplevel()
        audio_root.geometry('500x200')
        photo = PhotoImage(file="./logo.png")
        audio_root.iconphoto(False,photo)
        audio_root.resizable(0,0)
        audio_title = f'''{title[0:60]}\n{title[60:100]}..\n\nSong Duration: {duration}'''
        Label(audio_root,text=audio_title,font=("Arial",12)).place(x=10,y=10)
        
        b1 = Button(audio_root,text="Play",font=("ArialBlack",20),width=8,bd=5,command=lambda: Audio(vidlink,b1,b2,b3))
        b1.place(x=10,y=120)
        
        b2 = Button(audio_root,text="Pause/Play",font=("ArialBlack",20),width=9,bd=5,command=PAUSE)
        b2['state'] = DISABLED
        b2.place(x=167,y=120)
        
        b3 = Button(audio_root,text="Stop",font=("ArialBlack",20),width=8,bd=5,command=lambda: STOP(b1,b2,b3))
        b3['state'] = DISABLED
        b3.place(x=340,y=120)
        def on_closing():
            if askokcancel("Quit", "Do you want to quit?"):
                STOP(b1,b2,b3)
                audio_root.destroy()
        audio_root.protocol("WM_DELETE_WINDOW", on_closing)
        audio_root.mainloop()
        
    def PlayVideo(vidlink,title,duration):
        video_root = Toplevel()
        video_root.geometry('500x200')
        photo = PhotoImage(file="./logo.png")
        video_root.iconphoto(False,photo)
        video_root.resizable(0,0)
        
        audio_title = f'''{title[0:60]}\n{title[60:100]}..\n\nSong Duration: {duration}'''
        Label(video_root,text=audio_title,font=("Arial",12)).place(x=10,y=10)
        
        b1 = Button(video_root,text="Play",font=("ArialBlack",20),width=8,bd=5,command=lambda: Video(vidlink,b1,b2,b3))
        b1.place(x=10,y=120)
        
        b2 = Button(video_root,text="Pause/Play",font=("ArialBlack",20),width=9,bd=5,command=PAUSE)
        b2['state'] = DISABLED
        b2.place(x=167,y=120)
        
        b3 = Button(video_root,text="Stop",font=("ArialBlack",20),width=8,bd=5,command=lambda: STOP(b1,b2,b3))
        b3['state'] = DISABLED
        b3.place(x=340,y=120)
        
        def on_closing():
            if askokcancel("Quit", "Do you want to quit?"):
                STOP(b1,b2,b3)
                video_root.destroy()
        video_root.protocol("WM_DELETE_WINDOW", on_closing)
        video_root.mainloop()
    
    search=SearchVar.get()
    SearchData = list(SearchKeywords(search))

    Title = SearchData[2]
    ThumbURL = SearchData[3]
    Channel = SearchData[4]
    Duration = SearchData[5]
    Views = SearchData[6]

    raw_data1 = urllib.request.urlopen(ThumbURL[0]).read()
    im1 = Image.open(io.BytesIO(raw_data1))
    im1 = im1.resize((170,100))
    thumimage1 = ImageTk.PhotoImage(im1)
    label1 = Label(root, image=thumimage1)
    label1.place(x=30,y=200)
    Title1 = f'''{Title[0][0:75:]}\n{Title[0][75::]}'''
    Label(root,text=Title1,font=("ArialBlack",14),justify=LEFT).place(x=210,y=200)
    Label(root,text=Channel[0][0:25:]+" | ",font=("ArialBold",12)).place(x=210,y=250)
    Label(root,text=Views[0],font=("ArialBold",12)).place(x=400,y=250)
    Label(root,text="Video Length: "+Duration[0],font=("ArialBold",12)).place(x=210,y=275)
    Button(root,text="Play Audio",font=("ArialBlack",15),bd=5,command=lambda: PlayAudio(SearchData[1][0],Title[0],Duration[0])).place(x=620,y=240)
    Button(root,text="Play Video",font=("ArialBlack",15),bd=5,command=lambda: PlayVideo(SearchData[1][0],Title[0],Duration[0])).place(x=780,y=240)
    
    raw_data2 = urllib.request.urlopen(ThumbURL[1]).read()
    im2 = Image.open(io.BytesIO(raw_data2))
    im2 = im2.resize((170,100))
    thumimage2 = ImageTk.PhotoImage(im2)
    label2 = Label(root, image=thumimage2)
    label2.place(x=30,y=320)
    Title2 = f'''{Title[1][0:75:]}\n{Title[1][75::]}'''
    Label(root,text=Title2,font=("ArialBlack",14),justify=LEFT).place(x=210,y=320)
    Label(root,text=Channel[1][0:25:]+" | ",font=("ArialBold",12)).place(x=210,y=370)
    Label(root,text=Views[1],font=("ArialBold",12)).place(x=400,y=370)
    Label(root,text="Video Length: "+Duration[1],font=("ArialBold",12)).place(x=210,y=395)
    Button(root,text="Play Audio",font=("ArialBlack",15),bd=5,command=lambda: PlayAudio(SearchData[1][1],Title[1],Duration[1])).place(x=620,y=360)
    Button(root,text="Play Video",font=("ArialBlack",15),bd=5,command=lambda: PlayVideo(SearchData[1][1],Title[1],Duration[1])).place(x=780,y=360)
    
    raw_data3 = urllib.request.urlopen(ThumbURL[2]).read()
    im3 = Image.open(io.BytesIO(raw_data3))
    im3 = im3.resize((170,100))
    thumimage3 = ImageTk.PhotoImage(im3)
    label3 = Label(root, image=thumimage3)
    label3.place(x=30,y=440)
    Title3 = f'''{Title[2][0:75:]}\n{Title[2][75::]}'''
    Label(root,text=Title3,font=("ArialBlack",14),justify=LEFT).place(x=210,y=440)
    Label(root,text=Channel[2][0:25:]+" | ",font=("ArialBold",12)).place(x=210,y=490)
    Label(root,text=Views[2],font=("ArialBold",12)).place(x=400,y=490)
    Label(root,text="Video Length: "+Duration[2],font=("ArialBold",12)).place(x=210,y=515)
    Button(root,text="Play Audio",font=("ArialBlack",15),bd=5,command=lambda: PlayAudio(SearchData[1][2],Title[2],Duration[2])).place(x=620,y=480)
    Button(root,text="Play Video",font=("ArialBlack",15),bd=5,command=lambda: PlayVideo(SearchData[1][2],Title[2],Duration[2])).place(x=780,y=480)
    root.mainloop()

Label(root,text="Search Keywords:",font=("ArialBlack",15)).place(x=50,y=90)
e1 = Entry(root,font=("ArialBlack",20),width=50,bd=5,textvariable=SearchVar)
e1.focus()
e1.place(x=50,y=120)
Button(root,text="Search",font=("ArialBlack",20),bd=5,command=Search).place(x=840,y=110)

root.mainloop()