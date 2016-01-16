from django.contrib import admin
from .models import Data


class DataAdmin(admin.ModelAdmin):
    search_fields = ('title', 'date')
    list_display = ('title', 'date', 'type',)
    ordering = ['-date', ]


admin.site.register(Data, DataAdmin)
