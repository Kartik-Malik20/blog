from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    blog_cat = models.CharField(max_length=60,unique=True)
    blogcat_img = models.ImageField(upload_to='images/')
    blogcat_description=models.CharField(max_length=200)
    def __str__(self):
        return self.blog_cat
    
class Contact_info(models.Model):
    u_name = models.CharField(max_length=50)
    u_email = models.EmailField()
    u_message = models.CharField(max_length=200)

    def __str__(self):

        return self.u_email

class subscribe(models.Model):
    sub_email = models.EmailField()

    def __str__(self):

        return self.sub_email
        
from ckeditor.fields import RichTextField

class blog_post(models.Model):
    blog_name =models.CharField(max_length=100)
    cover_img=models.ImageField(upload_to='images/')
    blog_description=RichTextField()
    blogcat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    like_count=models.IntegerField(default=0, null=True)
    view_count=models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.blog_name
    
class comments(models.Model):
    u_comment = models.CharField(max_length=500)
    blog = models.ForeignKey(blog_post, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment on {self.blog}"
    
    
