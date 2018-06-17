from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model is always represented by class
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField()
    body  = models.TextField()
    #auto_add_now field will automatically assign a current date to the post we create
    date  = models.DateTimeField(auto_now_add=True)
    #first parameter-default image
    #second parameter is saying that it is not necessary
    thumb = models.ImageField(default='default.png', blank=True)
    #add in author later
    #default=none specify that there is always one user associated with an article
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title

    #takes self as a input which is the instance of the article
    def snippet(self):
        #so we want to cut down the body.we want to make it 50 characters long.
        return self.body[:50]+'...'
    
