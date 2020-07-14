from django.db import models

class photos(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='photos/',blank=False)
    def __str__(self):
        return self.title
