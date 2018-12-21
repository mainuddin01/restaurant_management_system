from django.conf.urls import url

from . import views

app_name = 'carts'

urlpatterns = [
    url(r'^tables/(?P<pk>\d+)/$', views.TableUserView.as_view(), name='table_user'),
]
