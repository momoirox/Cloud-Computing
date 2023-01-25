from django.contrib import admin

from .models import Student, Professor


# Register your models here.

class PmfAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


admin.site.register(Student, PmfAdmin)
admin.site.register(Professor)
