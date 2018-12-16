from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from string import ascii_lowercase


class HomePageView(LoginRequiredMixin, TemplateView):
    # template_name = 'home.html'
    template_name = 'home.html'
