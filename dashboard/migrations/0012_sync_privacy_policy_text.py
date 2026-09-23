# Gizlilik siyasəti mətni — content_defaults ilə sinxron

from django.db import migrations


def sync_privacy(apps, schema_editor):
    from dashboard.content_defaults import PRIVACY_DEFAULT

    AppContent = apps.get_model('dashboard', 'AppContent')
    AppContent.objects.update_or_create(
        key='privacy',
        defaults={'data': dict(PRIVACY_DEFAULT)},
    )


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_app_content_privacy'),
    ]

    operations = [
        migrations.RunPython(sync_privacy, migrations.RunPython.noop),
    ]
