from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.shortcuts import resolve_url,redirect
from .forms import SignUpForm, LoginForm
from django.conf import settings


class IndexView(TemplateView):
    template_name = "index.html"

class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        user.save()
        if user is not None:
            login(self.request, user)
            return redirect('work:index', user_id=user.id)
        return response


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    
    def get_success_url(self):
        return reverse_lazy('work:index', kwargs={'account_id': self.request.user.account_id})

class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:index")

class MyLogoutView(LogoutView):
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
@login_required
def my_logout_then_login(request, login_url=None):
    login_url = resolve_url(settings.LOGIN_URL)
    return MyLogoutView.as_view(next_page=login_url)(request)