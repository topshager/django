from django.contrib import admin
from .models import Member


class MemeberAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","joined_date")
admin.site.register(Member,MemeberAdmin)
