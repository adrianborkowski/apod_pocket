from django.contrib import admin
from .models import Data


class DataAdmin(admin.ModelAdmin):
    search_fields = ('title', 'created_date')
    list_display = ('title', 'created_date', 'media_type', 'concepts')
    ordering = ['-created_date', ]


admin.site.register(Data, DataAdmin)
