from django.db import models

# Create your models here.
class Appliances(models.Model):
    CATEGORY_CHOICES = [
        ('cooling', 'Cooling'),
        ('kitchen', 'Kitchen'),
        ('entertainment', 'Entertainment'),
        ('lighting', 'Lighting'),
        ('heating', 'Heating'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=255, null=True, blank=False)
    power_rating_watts = models.IntegerField(null=True, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.category}"

    class Meta:
        indexes = [
            models.Index(fields=['category', '-created_at']),
        ]

class Registration(models.Model):
    username = models.CharField(max_length=255, null=True, blank=False)
    password = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=False)

    def __str__(self):
        return f"{self.username} | {self.email}"

    class Meta:
        indexes = [
            models.Index(fields=['username']),
        ]