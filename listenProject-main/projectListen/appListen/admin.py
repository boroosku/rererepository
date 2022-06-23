from django.contrib import admin
from .models import SpotMusic

# Register your models here.
class SpotMusicAdmin(admin.ModelAdmin):
    list_display = ('user','song_author','song_title','song_image','audio','created_on')
admin.site.register(SpotMusic, SpotMusicAdmin)
