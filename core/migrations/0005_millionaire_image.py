# Generated by Django 4.0.3 on 2022-04-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_country_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='millionaire',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
