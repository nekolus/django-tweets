from django.db import models

# Create your models here.

class Post(models.Model):
    description = models.TextField()
    
    def __unicode__(self):
        return self.description