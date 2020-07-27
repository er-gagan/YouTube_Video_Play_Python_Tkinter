from youtube_search import YoutubeSearch
import vlc,pafy,time

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

def Audio(vidlink,duration):
    Vid_Duration_In_Second = sum(int(x) * 60 ** i for i, x in enumerate(reversed(duration.split(':'))))
    video = pafy.new(vidlink)
    bestaudio = video.getbestaudio()
    md = vlc.MediaPlayer(bestaudio.url)
    md.play()
    time.sleep(Vid_Duration_In_Second)
    
def Video(vidlink,duration):
    Vid_Duration_In_Second = sum(int(x) * 60 ** i for i, x in enumerate(reversed(duration.split(':'))))
    video = pafy.new(vidlink)
    video1 = video.streams[0]
    md = vlc.MediaPlayer(video1.url)
    md.play()
    time.sleep(Vid_Duration_In_Second)
