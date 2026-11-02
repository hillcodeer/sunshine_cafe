from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название блюда")
    price = models.IntegerField(verbose_name="Цена(сом)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name