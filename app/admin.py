from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pytje)
admin.site.register(Njoftime)
# admin.site.register(Video)


from embed_video.admin import AdminVideoMixin
class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)