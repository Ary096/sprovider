from django.db import models
from django.conf import settings
from django.db.models import Avg

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    average_rating = models.FloatField(default=0.0)  # New field
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.CharField(max_length=255, blank=True)  # Comma-separated tags

    def update_average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            self.average_rating = sum(r.rating for r in reviews) / reviews.count()
        else:
            self.average_rating = 0.0
        self.save()

    @property
    def aggregate_avg_rating(self):
        return self.reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    def __str__(self):
        return self.name
