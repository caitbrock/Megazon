# Generated by Django 4.0.6 on 2022-07-25 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_product_img_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='userProfileImages'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
