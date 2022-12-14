# Generated by Django 4.0.3 on 2022-05-27 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferenceform',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('politics', 'Politics'), ('covid-19', 'Covid-19'), ('trending', 'Trending'), ('international stories', 'International stories'), ('independent sources', 'Independent Sources'), ('sports', 'Sports')], default=2, max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpreferenceform',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
