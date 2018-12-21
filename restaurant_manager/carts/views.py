from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TableUserView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        context = {
            'mininavbar': True,
        }
        return render(request, 'carts/users_carts.html', context)
