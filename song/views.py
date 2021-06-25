from django.shortcuts import render
import song.models as models
from song.utils import analyzeTitle, getfromList
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib import messages
# Create your views here.
def song_list(request):
    songs = models.Song.objects.all().order_by('id')
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
                        s = models.Song.objects.create(name=name, artist=artist, type='techno')
                    except:
                        print('Error')
                    #s = models.Song.objects.savesong(name=name, artist=artist)
                    print('add')
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
