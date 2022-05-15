from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.views.generic import View
from django.shortcuts import redirect, render

from users.constants import USER_TYPES


User = get_user_model()

class RegistrationView(View):
    def get(self, request):
        user_types = dict(USER_TYPES)
        return render(request, 'users/registration.html', {'user_types': user_types})

    def post(self, request):
        data = request.POST.dict()
        username = data.get('username')
        password = data.get('password')
        account_type = data.get('account_type')

        try:
            user = User.objects.create_user(username=username, password=password)
            user.user_profile.type = account_type
            user.save()

            auth_user = authenticate(username=user.username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('core:millionaire_list_url')
            else:
                messages.add_message(request, messages.ERROR, 'Couldn\'t verify user for given credentials!')
                return redirect('users:registration_url')
        except Exception as e:
            messages.add_message(request, messages.ERROR, str(e))
            return redirect('users:registration_url')

registration_view = RegistrationView.as_view()


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        data = request.POST.dict()
        username = data.get('username')
        password = data.get('password')

        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            login(request, auth_user)
            return redirect('core:millionaire_list_url')
        else:
            messages.add_message(request, messages.ERROR, 'Couldn\'t verify user for given credentials!')
            return redirect('users:login_url')


login_view = LoginView.as_view()


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users:login_url')


logout_view = LogoutView.as_view()
