from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from accounts.models import Profile
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post-detail-category',kwargs = {'slug':self.name})

class Post(models.Model):
    statuses = [
        ("D","Draft"),
        ("P","Published"),
    ] 
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank = True)
    content = HTMLField()
    status = models.CharField(max_length=1,choices=statuses)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")
    image = models.ImageField(upload_to="blog/post",blank = True)
    author = models.ForeignKey(Profile,on_delete= models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs = {'slug':self.slug})

