# Mə inkar ədatı kind

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_app_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordmarknote',
            name='kind',
            field=models.CharField(
                choices=[
                    ('waqf_istinaf', 'Vəqf / İstinaf'),
                    ('qiraat', 'Qiraət Qeydi'),
                    ('ma_inkar', 'Mə inkar ədatı'),
                ],
                default='waqf_istinaf',
                max_length=20,
            ),
        ),
    ]
