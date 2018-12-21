from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from string import ascii_lowercase

from restaurant.models import Table


class HomePageView(LoginRequiredMixin, TemplateView):
    # template_name = 'home.html'
    template_name = 'table_selection.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['left_tables'] = Table.objects.filter(active=True, alignment='L')
        context['right_tables'] = Table.objects.filter(active=True, alignment='R')
        return context
