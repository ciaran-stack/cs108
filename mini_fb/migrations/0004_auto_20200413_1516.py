# Generated by Django 2.2.7 on 2020-04-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0003_auto_20200413_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmessage',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
