from django.dispatch import receiver
from django.db.models.signals import pre_save
from blog.models import Post

@receiver(pre_save,sender = Post)
def create_post(sender,**kwargs):
    print(sender)