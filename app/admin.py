from django.contrib import admin
from .models import SampleTable
# Register your models here.

class SampleTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(SampleTable, SampleTableAdmin)