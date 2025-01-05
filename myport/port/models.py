from django.db import models

# Create your models here.
class Yourself(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    degree=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    about_you=models.TextField()
    address=models.CharField(max_length=50)
    facebook=models.CharField(max_length=300,default='default_facebook_value')
    twitter=models.CharField(max_length=300,default='default_facebook_value')
    linkedin=models.CharField(max_length=300,default='default_facebook_value')
    github=models.CharField(max_length=300,default='default_facebook_value')


class category (models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(models.Model):
    category_id = models.ForeignKey(category,on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    content = models.TextField()
    cover_image = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
    
class Resume(models.Model):
    resume_image = models.FileField(upload_to='resume/')

    def __str__(self):
        return 'resume'
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    cover_image = models.FileField(upload_to='Blogimage/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
