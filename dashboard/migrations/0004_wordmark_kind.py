# Generated manually for Qiraət Qeydi

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_wordmark_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordmarknote',
            name='kind',
            field=models.CharField(
                choices=[
                    ('waqf_istinaf', 'Vəqf / İstinaf'),
                    ('qiraat', 'Qiraət Qeydi'),
                ],
                default='waqf_istinaf',
                max_length=20,
            ),
        ),
    ]
