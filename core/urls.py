from django.urls import path
from core.views import millionaire_list_view

app_name = 'core'
urlpatterns = [
    path('', millionaire_list_view, name='millionaire_list_url'),
]
