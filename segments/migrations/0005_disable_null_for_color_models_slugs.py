# Generated by Django 3.1.12 on 2021-06-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0004_add_slug_to_color_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=models.SlugField(max_length=45),
        ),
        migrations.AlterField(
            model_name='colortype',
            name='slug',
            field=models.SlugField(max_length=25, unique=True),
        ),
    ]
