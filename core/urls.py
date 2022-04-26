from django.urls import path
from core.views import millionaire_list_view, millionaire_vote_create_view

app_name = 'core'
urlpatterns = [
    path('', millionaire_list_view, name='millionaire_list_url'),
    path('vote/<int:millionaire_id>/', millionaire_vote_create_view, 
        name='millionaire_vote_create_url'),
]
