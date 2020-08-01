from youtube_search import YoutubeSearch
import vlc,pafy
from tkinter import *

def SearchKeywords(search):
    results = YoutubeSearch(search, max_results=3).to_dict()
    Vid_ID,Vid_Link,Vid_Title,Vid_Thumbnails,Vid_Channel,Vid_Duration,Vid_Views=[],[],[],[],[],[],[]
    for i in range(0,3):
        Vid_ID.append(results[i]['id'])
        vidlink = "https://www.youtube.com/watch?v="+Vid_ID[i]
        Vid_Link.append(vidlink)
        Vid_Title.append(results[i]['title'])
        Vid_Thumbnails.append(results[i]['thumbnails'][0])
        Vid_Channel.append(results[i]['channel'])
        Vid_Duration.append(results[i]['duration'])
        Vid_Views.append(results[i]['views'])
    return(Vid_ID,Vid_Link,Vid_Title,Vid_Thumbnails,Vid_Channel,Vid_Duration,Vid_Views)

md=None

def Audio(vidlink,b1,b2,b3):
    global md
    b1["state"] = DISABLED
    b2["state"] = ACTIVE
    b3["state"] = ACTIVE
    video = pafy.new(vidlink)
    bestaudio = video.getbestaudio()
    md = vlc.MediaPlayer(bestaudio.url)
    md.play()
    
def Video(vidlink,b1,b2,b3):
    global md
    b1["state"] = DISABLED
    b2["state"] = ACTIVE
    b3["state"] = ACTIVE
    video = pafy.new(vidlink)
    video1 = video.streams[0]
    md = vlc.MediaPlayer(video1.url)
    md.play()

def PAUSE():
    global md
    md.pause()
    
def STOP(b1,b2,b3):
    global md
    md.stop()
    b1["state"] = ACTIVE
    b2["state"] = DISABLED
    b3["state"] = DISABLED