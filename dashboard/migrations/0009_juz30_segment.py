from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_page_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juz30Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.JSONField(default=list, help_text='[{"verseKey":"78:1","position":1,"text":"..."}]')),
                ('color', models.CharField(default='#00897B', max_length=16)),
                ('summary_note', models.TextField(blank=True, default='', verbose_name='Xülasə qeydi')),
                ('azbar_note', models.TextField(blank=True, default='', verbose_name='Əzbər bölgü qeydi')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '30 cüz seqmenti',
                'verbose_name_plural': '30 cüz seqmentləri',
                'ordering': ['-updated_at'],
            },
        ),
    ]
