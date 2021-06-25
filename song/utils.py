from pytube import Playlist
import re
def getfromList(url, num=10):
    try:
        p = Playlist(url)
        print(f'{p.title}')
        list = []
        for video in p.videos[:int(num)]:
            list += [f'{video.title}']
        print(list)
        return list
    except:
        return None
def analyzeTitle(title:str):
    title_data = re.split('[-–]', title, 2)
    title_data = [x.strip() for x in title_data]
    return title_data