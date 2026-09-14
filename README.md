# Quran backend (Django + SQLite)

Expo (Tabyin) app və Miras dashboard üçün API: xülasələr, məshəf söz işarələri, qarilər.

## Qurulum (lokal)

```powershell
cd quran-backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
```

## İşə sal

```powershell
python manage.py runserver 0.0.0.0:8787
```

- Dashboard: `http://127.0.0.1:8787/`
- Health: `/api/health`

## DB

SQLite: `data/chat.db` (və ya `DATA_DIR/chat.db`). Dashboard əlavələri burada qalır.

## API

| Method | Path | Təsvir |
|--------|------|--------|
| GET | `/api/health` | Canlılıq |
| GET | `/api/xulaseler/` | Məal xülasələri |
| GET/POST | `/api/word-marks/` | Söz rəngləri |
| DELETE | `/api/word-marks/<id>/` | İşarə sil |

## Deploy (Render)

Root Directory: `quran-backend`. Persistent Disk + `DATA_DIR=/var/data`. Ətraflı: `render.yaml`.

App: `EXPO_PUBLIC_CHAT_API_URL=https://YOUR.onrender.com`
