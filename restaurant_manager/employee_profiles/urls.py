from django.conf.urls import url

from django.contrib.auth import views as auth_views
from . import views

app_name = 'employee_profiles'

urlpatterns = [
    url(r'^$', views.EmployeeList.as_view(), name='list'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='employee_profiles/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^create/$', views.CreateEmployee.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/detail/$', views.EmployeeDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.UpdateEmployee.as_view(), name='edit'),
]
