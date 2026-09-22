"""Dashboard giriş — /api/ və /admin/ açıq qalır."""

from urllib.parse import quote

from django.shortcuts import redirect
from django.urls import reverse


class DashboardLoginRequiredMiddleware:
    """HTML dashboard üçün login; sessiya bitənə / çıxışa qədər təkrar login yox."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path or '/'

        if self._is_exempt(path):
            return self.get_response(request)

        user = getattr(request, 'user', None)
        if user is not None and user.is_authenticated:
            return self.get_response(request)

        try:
            login_path = reverse('dash-login')
        except Exception:
            login_path = '/login/'

        nxt = path
        if request.META.get('QUERY_STRING'):
            nxt = f'{path}?{request.META["QUERY_STRING"]}'
        return redirect(f'{login_path}?next={quote(nxt, safe="/")}')

    @staticmethod
    def _is_exempt(path: str) -> bool:
        if path.startswith('/api/'):
            return True
        if path.startswith('/admin/'):
            return True
        if path.startswith('/static/') or path.startswith('/media/'):
            return True
        if path.rstrip('/') in ('/login', '/logout'):
            return True
        if path.startswith('/login/') or path.startswith('/logout/'):
            return True
        return False
