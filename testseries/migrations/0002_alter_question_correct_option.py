# Generated by Django 3.2.3 on 2024-07-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testseries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.CharField(choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3'), ('option4', 'Option 4')], max_length=50),
        ),
    ]