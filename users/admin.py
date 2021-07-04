from django.contrib import admin
from .models import UserProfile,UserVideo,UserPlayList,Comments
# Register your models here.
admin.site.register(UserVideo)
admin.site.register(UserProfile)
admin.site.register(UserPlayList)
admin.site.register(Comments)

