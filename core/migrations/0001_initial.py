# Generated by Django 4.0.3 on 2022-03-23 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Millionaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
    ]
