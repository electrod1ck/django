# Generated by Django 4.2.17 on 2025-02-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_herosection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='backgrounds/', verbose_name='Фон сайта')),
            ],
        ),
    ]
