from django.shortcuts import render
import song.models as models
from song.utils import analyzeTitle, getfromList
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib import messages
# Create your views here.
def song_list(request):
    songs = models.Song.objects.all().order_by('id')
    [song for song in songs]
    artists = set([song.artist for song in songs])
    if 'artist' in request.GET:
        if request.GET['artist'] == 'all' or request.GET['artist'] == '':
            return render(request, 'home.html', locals())
        songs = songs.filter(artist=request.GET['artist'])
        return render(request, 'home.html', locals())
    return render(request, 'home.html', locals())

def addsong(request):
    try:
        if request.method == 'POST':
            url = request.POST.get('url')
            num = request.POST.get('num')
            song_list = getfromList(url, int(num))
            print(f'List:{song_list}')
            if song_list != None:
                for song in song_list:
                    data = analyzeTitle(song)
                    name = data[1] if len(data) > 1 else data[0]
                    artist = data[0] if len(data) > 1 else 'Unknown'
                    print('ready to add')
                    try:
                        s = models.Song.objects.savesong(name=name, artist=artist)
                    except:
                        print(f'can\'t add {name}')
                    data.clear()
                messages.success(request, 'Success')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Please Enter Right URL')
                return render(request, 'addsong.html')
        else:
            return render(request, 'addsong.html')
    except:
        return HttpResponseRedirect('/')

def intro(request):
    song = models.Song.objects.filter(id=request.GET['id'])[0]
    try:
        intro = models.Intro.objects.filter(song=song)[0]
    except:
        print('No intro')
    return render(request, 'song_intro.html', locals())