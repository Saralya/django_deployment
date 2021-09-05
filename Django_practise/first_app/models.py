from django.db import models
from django.urls import reverse

# Create your models here

class Musician(models.Model):
	# id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name+ ' ' + self.last_name   #ei function tar kaj hocche object er value return kora

    def get_absolute_url(self):
        return reverse("first_app:content")
        # reverse function ta decide kore AddMusician form submit howar por kon page e niye jabe
        # return reverse("first_app:content", kwargs={'pk':self.pk})
        # eta use korbo jodi id dhore kono kaj kora lage

class Album(models.Model):
	# id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_list')
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    #rating akta tuple jeta num_stars er choice (dropdown) hisebe ashbe
    #rating tuple tar 1st parameter ta database e save hoy, 2nd ta front end e show hoy
    #1st parameter integer bole num_stars e IntegerField lekha hoise 
    rating = (
        (1, "worst"),
        (2, "bad"),
        (3, "not bad"),
        (4, "good"),
        (5, "excellent"),
    )
    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return self.name + ', Rating: ' + str(self.num_stars)