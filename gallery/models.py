from django.db import models
from django.db import models
from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class HeroSection(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    text = models.CharField(max_length=255, default="ГЛАВНЫЙ ТЕКСТ")

    def __str__(self):
        return self.text


class Background(models.Model):
    image = models.ImageField(upload_to='backgrounds/', verbose_name="Фон сайта")

    def __str__(self):
        return "Фон сайта"


