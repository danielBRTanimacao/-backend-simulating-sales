from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class ProductForSale(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    posted_date = models.DateField(default=timezone.now)
    img = models.ImageField(blank=True, upload_to='images/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} {self.value}'