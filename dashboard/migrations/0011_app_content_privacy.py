# Gizlilik siyasəti — AppContent key

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_merge_0008_alter_0009_juz30'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appcontent',
            name='key',
            field=models.SlugField(
                choices=[
                    ('about', 'Haqqında'),
                    ('privacy', 'Gizlilik siyasəti'),
                    ('meal_intro', 'Məal giriş'),
                    ('reciters', 'Qarilər'),
                    ('telegram', 'Telegram'),
                ],
                max_length=40,
                unique=True,
            ),
        ),
    ]
