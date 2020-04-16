# Generated by Django 2.2.7 on 2020-04-13 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0002_statusmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusmessage',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini_fb.Profile'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(blank=True)),
                ('image_file', models.ImageField(blank=True, upload_to='')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini_fb.Profile')),
            ],
        ),
    ]
