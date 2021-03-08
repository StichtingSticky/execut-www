from django.urls import path, include

from . import views
from core import views as core_views

app_name = "pages"

urlpatterns = [
    path('', views.view_page, name='view_home'),
    path('speakers/', core_views.speakers, name='view_speakers'),
    path('partners/', core_views.sponsors, name='view_sponsors'),
    path('programme/', core_views.programme, name='view_programme'),
    path('<slug:slug>/', views.view_page, name='view_page'),
    path('speakers/<int:speaker_id>/<slug:speaker_slug>', core_views.single_speaker, name='single_speaker')
]