from django.contrib import admin
from .models import Category,Contact_info,subscribe,blog_post,comments
# Register your models here.

admin.site.register(Category)
admin.site.register(Contact_info)
admin.site.register(subscribe)
admin.site.register(blog_post)
admin.site.register(comments)