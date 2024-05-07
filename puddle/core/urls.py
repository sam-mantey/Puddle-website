from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.Index, name='index'),
    path("contact/", views.Contact, name="contact"),
    path("signup/", views.SignUp, name="signup"),
    path("login/", auth_view.LoginView.as_view(template_name="core/login.html",authentication_form=LoginForm), name="login"),
]