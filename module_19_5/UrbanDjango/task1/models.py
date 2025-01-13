from django.db import models


# Create your models here.

class Buyer(models.Model):  # покупатель
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=150, decimal_places=4)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):  # игра
    title = models.CharField(max_length=100)  # название игры
    cost = models.DecimalField(max_digits=150, decimal_places=4)
    size = models.DecimalField(max_digits=150, decimal_places=4)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title


class News(models.Model):  # Новости
    title = models.CharField(max_length=200)  # название игры
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
