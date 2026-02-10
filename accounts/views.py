from django.shortcuts import render
from django.views.generic import TemplateView


class Login(TemplateView):
    template_name = 'login.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
