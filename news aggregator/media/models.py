from django.contrib.auth.models import AbstractUser
from django.db import models

#user model
class User(AbstractUser):
    pass

class News(models.Model):
    title = models.CharField(max_length=250)
    #storing images but its also okay not to have them.
    image = models.URLField(null=True, blank=True)
    url = models.TextField()

    #once info is gathered return the title of the thing.(always at least needs to have a title.)
    def __str__(self):
        return self.title
