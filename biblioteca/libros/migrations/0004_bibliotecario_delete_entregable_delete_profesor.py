# Generated by Django 4.2 on 2024-07-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bibliotecario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
