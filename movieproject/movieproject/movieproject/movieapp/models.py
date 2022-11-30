from django.db import models

class Movies(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='galary')

    def __str__(self):
        return self.name