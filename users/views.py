from django.views.generic import View
from django.shortcuts import redirect, render


class RegistrationView(View):
    def get(self, request):
        return render(request, 'users/registration.html')

    def post(self, request):
        return redirect('core:millionaire_list_url')


registration_view = RegistrationView.as_view()


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        return redirect('core:millionaire_list_url')


login_view = LoginView.as_view()
