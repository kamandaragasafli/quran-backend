from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='dash-home'),
    path('xulaseler/', views.summaries, name='dash-summaries'),
    path('quran/', views.quran, name='dash-quran'),
    path('quran/fonts/<str:filename>', views.mushaf_font, name='dash-mushaf-font'),
    path('qariler/', views.reciters, name='dash-reciters'),
]
