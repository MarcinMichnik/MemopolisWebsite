# Generated by Django 3.0.6 on 2020-07-04 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memopolis', '0020_auto_20200630_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_id',
            new_name='author',
        ),
    ]