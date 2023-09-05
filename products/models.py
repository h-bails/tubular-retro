from django.db import models


class Category(models.Model):
    '''Model for the categories'''
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    '''Model for the products'''
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=1000)
    measurements = models.CharField(max_length=254)
    condition = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    date_added = models.DateField(auto_now=True)
    image_1 = models.ImageField(null=True, blank=True)
    is_sold = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_sold']

    def __str__(self):
        return self.name
