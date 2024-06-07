from django.contrib import admin
from .models import RedgModel

# Register your models here.
@admin.register(RedgModel)
class RedgModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'dept', 'mark', 'email')