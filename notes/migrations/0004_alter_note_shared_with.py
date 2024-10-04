# Generated by Django 3.2.3 on 2024-07-19 11:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0003_alter_note_shared_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_notes', to=settings.AUTH_USER_MODEL),
        ),
    ]