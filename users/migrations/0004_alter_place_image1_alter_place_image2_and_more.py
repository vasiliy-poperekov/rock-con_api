# Generated by Django 4.1.1 on 2022-11-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_image_rename_photo_groupsinger_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='place',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
