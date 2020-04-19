from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth.models import Group


@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)
        group = Group.objects.get(name = "Author")
        instance.groups.add(group)


