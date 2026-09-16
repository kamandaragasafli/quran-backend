# Telegram AppContent key

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_ma_inkar_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appcontent',
            name='key',
            field=models.SlugField(
                choices=[
                    ('about', 'Haqqında'),
                    ('meal_intro', 'Məal giriş'),
                    ('reciters', 'Qarilər'),
                    ('telegram', 'Telegram'),
                ],
                max_length=40,
                unique=True,
            ),
        ),
    ]
