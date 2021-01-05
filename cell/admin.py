from django.contrib import admin
from .models import cellf


class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'date',)


admin.site.register(cellf, HomeAdmin)

# Register your models here.
