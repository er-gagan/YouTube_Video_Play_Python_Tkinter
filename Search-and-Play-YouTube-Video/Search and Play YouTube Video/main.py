from youtube_search import YoutubeSearch
import vlc,pafy,time

results = YoutubeSearch('Guru Randhawa: High Rated Gabru Official Song', max_results=1).to_dict()

Vid_ID = results[0]['id']
Vid_Link = "https://www.youtube.com/watch?v="+Vid_ID
Vid_Title = results[0]['title'][0:50:]+'...'
Vid_Thumbnails = results[0]['thumbnails'][0]
Vid_Channel = results[0]['channel']
Vid_Duration = results[0]['duration']
Vid_Views = results[0]['views']
print(Vid_Link)
print(Vid_Title)
print(Vid_Thumbnails)
print(Vid_Channel)
print(Vid_Duration)
print(Vid_Views)

Vid_Duration_In_Second = sum(int(x) * 60 ** i for i, x in enumerate(reversed(Vid_Duration.split(':'))))

video = pafy.new(Vid_Link)
best = video.getbestaudio()
md = vlc.MediaPlayer(best.url)
md.play()
time.sleep(Vid_Duration_In_Second)
