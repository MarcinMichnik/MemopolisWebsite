# Generated by Django 3.0.6 on 2020-06-13 00:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memopolis', '0008_auto_20200612_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meme',
            name='num_vote_down',
        ),
        migrations.RemoveField(
            model_name='meme',
            name='num_vote_up',
        ),
        migrations.RemoveField(
            model_name='meme',
            name='vote_score',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('upvoted_by', models.TextField(null=True)),
                ('downvoted_by', models.TextField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]