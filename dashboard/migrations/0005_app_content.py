# Generated manually for AppContent (Haqqında / Məal giriş / Qarilər)

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_wordmark_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'key',
                    models.SlugField(
                        choices=[
                            ('about', 'Haqqında'),
                            ('meal_intro', 'Məal giriş'),
                            ('reciters', 'Qarilər'),
                        ],
                        max_length=40,
                        unique=True,
                    ),
                ),
                ('data', models.JSONField(blank=True, default=dict)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Tətbiq mətnı',
                'verbose_name_plural': 'Tətbiq mətnləri',
                'ordering': ['key'],
            },
        ),
    ]
