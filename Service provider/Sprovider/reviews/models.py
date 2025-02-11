from django.db import models
from django.conf import settings
from services.models import Service

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.service.name} - ({self.rating} Stars)"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.service.update_average_rating()  # Update rating when a review is saved
