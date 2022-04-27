# Generated by Django 4.0.3 on 2022-04-26 23:52

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_millionaire_vector_column_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='millionaire',
            name='core_millio_name_b48509_idx',
        ),
        migrations.RemoveIndex(
            model_name='millionaire',
            name='core_millio_vector__32459a_gin',
        ),
        migrations.AddIndex(
            model_name='millionaire',
            index=django.contrib.postgres.indexes.GinIndex(fields=['vector_column'], name='millionaire_vector__6513e8_gin'),
        ),
        migrations.AddIndex(
            model_name='millionaire',
            index=models.Index(fields=['name', 'profession'], name='millionaire_name_a7bba0_idx'),
        ),
        migrations.AlterModelTable(
            name='millionaire',
            table='millionaire',
        ),
    ]