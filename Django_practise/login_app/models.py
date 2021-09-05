from django.db import models
from django.contrib.auth.models import User
# User is a built-in model of django for login purpose (see in admin panel)



class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # UserInfo model er 1ta entry, User model er only 1ta entry er sathe connected thakbe..
    fb_id = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username  # User model theke username field ta return korbe
