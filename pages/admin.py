from django.contrib import admin
from .models import Team
#from .models import Picture

from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    list_display = ('id', 'thumbnail','first_name')
    

# Register your models here.
admin.site.register(Team, TeamAdmin)

#admin.site.register(Picture)


