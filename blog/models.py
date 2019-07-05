from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    # tags = ListField()
    thumbnail = models.CharField(max_length=100)
    createdAt = models.DateTimeField()
    def __str__(self):
        return self.title