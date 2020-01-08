from django.contrib import admin
from .models import Url
# Register your models here.
class UrlsAdmin(admin.ModelAdmin):
    list_display= ('shorten_id', 'original_url')


admin.site.register(Url, UrlsAdmin)