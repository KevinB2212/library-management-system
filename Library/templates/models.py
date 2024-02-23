from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    category = models.CharField(max_length=255, default='uncategorized')

    def __str__(self):
        return self.title

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title