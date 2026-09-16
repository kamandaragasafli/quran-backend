from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='dash-home'),
    path('xulaseler/', views.summaries, name='dash-summaries'),
    path('haqqinda/', views.about_content, name='dash-about'),
    path('meal-giris/', views.meal_intro_content, name='dash-meal-intro'),
    path('telegram/', views.telegram_content, name='dash-telegram'),
    path('quran/', views.quran, name='dash-quran'),
    path('quran/fonts/<str:filename>', views.mushaf_font, name='dash-mushaf-font'),
    path('qariler/', views.reciters, name='dash-reciters'),
]
