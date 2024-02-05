from .models import Category,blog_post,comments
from django.forms import ModelForm

class Blog_Form(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogPost_Form(ModelForm):
    class Meta:
         model = blog_post
         fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model = comments
        fields = ['u_comment']