from django.urls import path

from . import views

urlpatterns = [
    path('health', views.health),
    path('health/', views.health),
    path('app-content', views.app_content_pack),
    path('app-content/', views.app_content_pack),
    path('app-content/<str:key>', views.app_content_detail),
    path('app-content/<str:key>/', views.app_content_detail),
    path('xulaseler', views.meal_summaries),
    path('xulaseler/', views.meal_summaries),
    path('quran-meal-notes', views.meal_summaries),
    path('quran-meal-notes/', views.meal_summaries),
    path('word-marks', views.word_marks),
    path('word-marks/', views.word_marks),
    path('word-marks/<int:note_id>', views.word_mark_detail),
    path('word-marks/<int:note_id>/', views.word_mark_detail),
    path('page-notes', views.page_notes),
    path('page-notes/', views.page_notes),
    path('page-notes/<int:note_id>', views.page_note_detail),
    path('page-notes/<int:note_id>/', views.page_note_detail),
    path('juz30-segments', views.juz30_segments),
    path('juz30-segments/', views.juz30_segments),
    path('juz30-segments/<int:note_id>', views.juz30_segment_detail),
    path('juz30-segments/<int:note_id>/', views.juz30_segment_detail),
    path('groups', views.list_groups),
    path('groups/', views.list_groups),
    path('groups/<str:group_id>', views.get_group),
    path('groups/<str:group_id>/', views.get_group),
    path('groups/<str:group_id>/messages', views.group_messages),
    path('groups/<str:group_id>/messages/', views.group_messages),
]
