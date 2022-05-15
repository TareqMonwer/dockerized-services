from django.urls import path

from users.views import registration_view, login_view, logout_view


app_name = 'users'
urlpatterns = [
    path('registration/', registration_view, name='registration_url'),
    path('login/', login_view, name='login_url'),
    path('logout/', logout_view, name='logout_url'),
]
