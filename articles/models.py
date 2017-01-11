from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    summary = models.TextField()
    main_text = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title