from django.db import models

class Settings(models.Model):
    google_keep_movies_note_id = models.CharField(max_length=300, blank=True)

class Movie(models.Model):
    google_keep_item_id = models.CharField(
        max_length=300, 
        db_index=True
    )
    google_keep_text = models.CharField(
        max_length=500, 
        blank=True
    )
    google_keep_checked = models.BooleanField()

    imdb_id = models.CharField(
        max_length=50, 
        db_index=True
    )
    imdb_title = models.CharField(
        max_length=300
    )
    imdb_year = models.IntegerField()
    imdb_release_date = models.DateField()
    imdb_runtime_minutes = models.IntegerField()
    imdb_awards = models.CharField(
        max_length=1000
    )
    imdb_image = models.CharField(
        max_length=500
    )
    watched = models.BooleanField()