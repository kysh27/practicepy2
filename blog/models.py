from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    address = models.TextField()
    contactnum = models.CharField(max_length=20)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
    
    def __str__(self):
        return self.user.username