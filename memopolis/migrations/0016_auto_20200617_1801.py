# Generated by Django 3.0.6 on 2020-06-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memopolis', '0015_auto_20200617_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]