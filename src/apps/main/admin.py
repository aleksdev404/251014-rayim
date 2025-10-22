from django.contrib import admin

from . import models


@admin.register(models.Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    list_display = ('title', )
