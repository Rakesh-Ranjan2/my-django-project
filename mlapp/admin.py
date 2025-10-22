from django.contrib import admin
from .models import PlantImage

@admin.register(PlantImage)
class PlantImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'prediction', 'certainity', 'uploaded_at')