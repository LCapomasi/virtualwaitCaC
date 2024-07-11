# Generated by Django 4.2.13 on 2024-07-10 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_rename_about_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'proyecto', 'verbose_name_plural': 'proyectos'},
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]