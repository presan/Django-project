from django.contrib import admin
from myapp.models import Post

# Register your models here.

class Postadmin(admin.ModelAdmin):
    pass

admin.site.register(Post,Postadmin)