from django.contrib import admin

from programs import models


@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    pass
