# Generated by Django 4.0.3 on 2022-04-27 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0012_create_trigger'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(default='system_default.png', upload_to='profile_pics/')),
                ('about', models.CharField(blank=True, max_length=255, null=True)),
                ('last_seen', models.DateTimeField(auto_now_add=True)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.PositiveSmallIntegerField(choices=[('Millionaire', 0), ('Business', 1), ('Admin', 2), ('User', 3)], default=3)),
                ('lives_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles_lives_in', to='core.country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('works_at', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees_works_at', to='core.company')),
            ],
            options={
                'ordering': ['-joined_at'],
            },
        ),
    ]