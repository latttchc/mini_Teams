from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("accounts/", views.IndexView.as_view(), name="index"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('accounts/login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.my_logout_then_login, name="logout"),
]

