# Serverdə yaranmış; repo ilə sinxron (0008_page_note ilə paralel)

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_app_content_telegram'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='summarynote',
            options={
                'ordering': ['-updated_at'],
                'verbose_name': 'Xülasə',
                'verbose_name_plural': 'Xülasələr',
            },
        ),
        migrations.AlterModelOptions(
            name='wordmarknote',
            options={
                'ordering': ['-updated_at'],
                'verbose_name': 'Söz rəngi / işarə',
                'verbose_name_plural': 'Söz rəngləri (vəqf · qiraət · مَا)',
            },
        ),
    ]
