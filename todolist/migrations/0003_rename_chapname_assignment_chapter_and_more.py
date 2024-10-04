# Generated by Django 5.0.6 on 2024-07-13 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_remove_assignment_name_remove_selfstudy_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='chapname',
            new_name='chapter',
        ),
        migrations.RenameField(
            model_name='assignment',
            old_name='due_date',
            new_name='deadline',
        ),
        migrations.RenameField(
            model_name='assignment',
            old_name='subname',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='selfstudy',
            old_name='due_date',
            new_name='deadline',
        ),
        migrations.RenameField(
            model_name='selfstudy',
            old_name='chapname',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='selfstudy',
            name='subname',
        ),
    ]