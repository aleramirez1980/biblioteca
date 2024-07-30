# Generated by Django 4.2 on 2024-07-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('año', models.IntegerField()),
            ],
        ),
    ]
