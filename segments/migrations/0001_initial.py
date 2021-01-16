# Generated by Django 3.1.5 on 2021-01-16 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='ColorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Фактура')),
            ],
            options={
                'verbose_name': 'Фактура',
                'verbose_name_plural': 'Фактуры',
            },
        ),
        migrations.CreateModel(
            name='OrderNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Номер заказа')),
            ],
            options={
                'verbose_name': 'Номер заказа',
                'verbose_name_plural': 'Номера заказов',
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Расположение')),
            ],
            options={
                'verbose_name': 'Расположение',
                'verbose_name_plural': 'Расположения',
            },
        ),
        migrations.CreateModel(
            name='SegmentOld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=15)),
                ('color', models.CharField(blank=True, max_length=15)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('square', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('order_number', models.CharField(blank=True, max_length=15)),
                ('rack', models.CharField(blank=True, max_length=20)),
                ('defect', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'segment',
            },
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField(verbose_name='Ширина')),
                ('height', models.IntegerField(verbose_name='Высота')),
                ('square', models.FloatField(blank=True, null=True, verbose_name='Площадь отрезка')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.DateTimeField(auto_now=True)),
                ('defect', models.BooleanField(default=False, verbose_name='Дефектный')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='segments', to='segments.color', verbose_name='Цвет')),
                ('order_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='segments', to='segments.ordernumber', verbose_name='Номер заказа')),
                ('rack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='segments', to='segments.rack', verbose_name='Расположение')),
            ],
            options={
                'verbose_name': 'Отрезок',
                'verbose_name_plural': 'Отрезки',
            },
        ),
        migrations.AddField(
            model_name='color',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='segments.colortype'),
        ),
    ]
