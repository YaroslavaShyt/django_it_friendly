# Generated by Django 4.2 on 2023-04-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_friendly', '0004_studying_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400)),
                ('answer', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='StudyingDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='StudyingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=400)),
                ('duties', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Studying',
        ),
    ]
