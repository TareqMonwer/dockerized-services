from django.urls import path
from core.constants import TOP_MILLIONAIRES_COUNT
from core.views import (millionaire_list_view, millionaire_vote_create_view,
                        top_millionaires_index_view,)

app_name = 'core'
urlpatterns = [
    path('', millionaire_list_view, name='millionaire_list_url'),
    path(f'top{TOP_MILLIONAIRES_COUNT}/', top_millionaires_index_view, 
        name='top_millionaires_index_url'),
    path('vote/<int:millionaire_id>/', millionaire_vote_create_view, 
        name='millionaire_vote_create_url'),
]
