#!/usr/bin/env bash
# Render / production start — static + migrate, sonra gunicorn
set -euo pipefail
cd "$(dirname "$0")/.."

python manage.py collectstatic --noinput
python manage.py migrate --noinput
exec gunicorn config.wsgi:application \
  --bind "0.0.0.0:${PORT:-8000}" \
  --workers "${WEB_CONCURRENCY:-2}" \
  --timeout 120 \
  --access-logfile - \
  --error-logfile -
