# Generated by Django 2.1.1 on 2018-09-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='death_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='middle_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='author',
            name='pseudonym',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
