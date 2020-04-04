# Generated by Django 2.2.7 on 2020-04-03 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_quote_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='author',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='image_url',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(blank=True)),
                ('person', models.ForeignKey(on_delete='Cascade', to='quotes.Person')),
            ],
        ),
    ]
