from django.shortcuts import render
from .models import HeroSection, Photo, Background

def gallery_view(request):
    hero = HeroSection.objects.first()  # Получаем первую запись с главной фотографией и текстом
    photos = Photo.objects.all()
    background = Background.objects.first()  # Получаем фон, если он есть


    return render(request, 'gallery/index.html', {
        'hero_image_url': hero.image.url if hero else '',
        'hero_text': hero.text if hero else '',
        'background_image_url': background.image.url if background else '',
        'photos': photos,
    })