from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_app_content_telegram'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.PositiveSmallIntegerField(db_index=True, unique=True)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Səhifə qeydi',
                'verbose_name_plural': 'Səhifə qeydləri',
                'ordering': ['page'],
            },
        ),
    ]
