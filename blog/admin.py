from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(Blog)
admin.site.register(UserBlog)
admin.site.register(Message)
admin.site.register(Test)