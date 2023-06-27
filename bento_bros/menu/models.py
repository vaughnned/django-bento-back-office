from django.db import models

# Create your models here.


class Appetizer(models.Model):
    name = models.CharField(max_length=50)
    japanese_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=150)
    # id = models.IntegerField(primary_key=True, default=0)

    def __str__(self):
        return self.name


class MainCourse(models.Model):
    name = models.CharField(max_length=50)
    japanese_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=150)
    # id = models.IntegerField(primary_key=True, default=0)

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(max_length=50)
    japanese_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=150)
    # id = models.IntegerField(primary_key=True, default=0)

    def __str__(self):
        return self.name
