# Generated by Django 2.2.7 on 2020-04-04 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_quote_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='person',
            field=models.ForeignKey(on_delete='CASCADE', to='quotes.Person'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='person',
            field=models.ForeignKey(on_delete='CASCADE', to='quotes.Person'),
        ),
    ]
