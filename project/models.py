from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ProductForSale(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    posted_date = models.DateField(default=timezone.now)
    img = models.ImageField(blank=True, upload_to='images/%Y/%m/')
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.value}'