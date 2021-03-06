from django.db import models

# Create your models here.
class SongManager(models.Manager):
    def savesong(self, name, artist='Unknown', type='Unknown'):
        print(f'Data:{name} {artist} {type}')
        if len(Song.objects.filter(name=name)) > 0:
            return False
        else:
            print('try to add')
            song = self.create(name=name, artist=artist, type=type)
            print(song.name)
        return song

class Song(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    objects = SongManager()
    def __str__(self):
        return self.name

class Intro(models.Model):
    date = models.DateField(auto_now=True)
    content = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)