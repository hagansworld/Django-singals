from django.shortcuts import render

# Create your views here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print("Profile created")


# connect a receiver to a sender
# The receiver is the created profile and sender is the model that will trigger it
post_save.connect(create_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print("Profile updated!")


post_save.connect(update_profile, sender=User)

# the problem with the code is that when we try to  update the main user
#  it gives an error because the instance was set on the Model Profile with user instance
