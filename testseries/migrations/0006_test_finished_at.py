# Generated by Django 5.0.4 on 2024-08-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testseries', '0005_remove_test_shared_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]