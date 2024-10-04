# Generated by Django 3.2.3 on 2024-07-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testseries', '0002_alter_question_correct_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option1_image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/options/'),
        ),
        migrations.AddField(
            model_name='question',
            name='option2_image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/options/'),
        ),
        migrations.AddField(
            model_name='question',
            name='option3_image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/options/'),
        ),
        migrations.AddField(
            model_name='question',
            name='option4_image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/options/'),
        ),
        migrations.AddField(
            model_name='question',
            name='text_image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/images/'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]