# Generated by Django 2.1.1 on 2018-09-06 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=25)),
                ('second_name', models.CharField(max_length=25)),
                ('middle_name', models.CharField(max_length=25)),
                ('pseudonym', models.CharField(max_length=25)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField()),
                ('biography', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80, unique=True)),
                ('year', models.IntegerField()),
                ('number_page', models.IntegerField()),
                ('description', models.TextField()),
                ('cover', models.ImageField(upload_to='')),
                ('authors', models.ManyToManyField(to='mylib.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=35)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylib.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='mylib.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylib.PublishingHouse'),
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylib.Country'),
        ),
        migrations.AddField(
            model_name='author',
            name='genre',
            field=models.ManyToManyField(to='mylib.Genre'),
        ),
    ]
