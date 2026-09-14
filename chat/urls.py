from django.urls import path

from . import views

urlpatterns = [
    path('health', views.health),
    path('health/', views.health),
    path('xulaseler', views.meal_summaries),
    path('xulaseler/', views.meal_summaries),
    path('quran-meal-notes', views.meal_summaries),
    path('quran-meal-notes/', views.meal_summaries),
    path('word-marks', views.word_marks),
    path('word-marks/', views.word_marks),
    path('word-marks/<int:note_id>', views.word_mark_detail),
    path('word-marks/<int:note_id>/', views.word_mark_detail),
    path('groups', views.list_groups),
    path('groups/', views.list_groups),
    path('groups/<str:group_id>', views.get_group),
    path('groups/<str:group_id>/', views.get_group),
    path('groups/<str:group_id>/messages', views.group_messages),
    path('groups/<str:group_id>/messages/', views.group_messages),
]
