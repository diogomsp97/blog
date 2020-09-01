from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kawrgs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def saveProfile(sender, instance, **kawrgs):
    instance.profile.save()