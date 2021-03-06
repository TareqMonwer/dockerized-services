# Generated by Django 4.0.3 on 2022-04-26 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_millionaire_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='millionaire',
            name='image',
            field=models.ImageField(default='system_default.png', upload_to='profile_pics/'),
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['name'], name='core_compan_name_f8e523_idx'),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['name'], name='core_countr_name_5737bb_idx'),
        ),
        migrations.AddIndex(
            model_name='millionaire',
            index=models.Index(fields=['name', 'profession'], name='core_millio_name_b48509_idx'),
        ),
    ]
