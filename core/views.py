from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView


class CustomLoginView(LoginView):
    template_name = "registration/login.html"

class LoggedView(LoginRequiredMixin, TemplateView):
    template_name = "registration/logged.html"

@login_required
def home(request):
    return redirect('logged')
