from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50)
    created = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    