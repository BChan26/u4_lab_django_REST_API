from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('',views.TeamList.as_view(), name='team_list'),
    path('players/',views.PlayerList.as_view(), name='player_list'),
    path('teams/<int:pk>',views.TeamDetail.as_view(), name='team_detail'),
    path('players/<int:pk>',views.PlayerDetail.as_view(), name='player_detail'),
]