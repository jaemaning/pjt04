from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    realease_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.URLField(max_length=300, blank=True)
    description = models.TextField()
    actor_image = models.ImageField(blank=True)
    
    def __str__(self):
        return f"{self.pk}번째 영화 - {self.title}"