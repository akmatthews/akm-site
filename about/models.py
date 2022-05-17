from django.db import models

class About(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    image = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    facebook_url = models.CharField(max_length=500, blank=True)
    twitter_url = models.CharField(max_length=500, blank=True)
    youtube_url = models.CharField(max_length=500, blank=True)
    instagram_url = models.CharField(max_length=500, blank=True)
