from django.db import models

class PlantImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    prediction = models.CharField(max_length=100, blank=True, null=True)
    certainity = models.FloatField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image.name} ({self.prediction or 'Unpredicted'})"
