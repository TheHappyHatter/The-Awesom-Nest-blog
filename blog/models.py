from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title