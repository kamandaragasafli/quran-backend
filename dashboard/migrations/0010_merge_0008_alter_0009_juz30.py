# 0008_alter_* və 0009_juz30_segment leaf-lərini birləşdirir

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_summarynote_options_alter_wordmarknote_options'),
        ('dashboard', '0009_juz30_segment'),
    ]

    operations = []
