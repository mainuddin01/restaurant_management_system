from django.conf.urls import url

from . import views

app_name = 'restaurant'

urlpatterns = [
    url(r'^tables/$', views.TableListView.as_view(), name='table_list'),
    url(r'^tables/(?P<pk>\d+)/$', views.TableDetailView.as_view(), name='table_detail'),
    url(r'^tables/create/$', views.TableCreateView.as_view(), name='table_create'),
    url(r'^tables/(?P<pk>\d+)/edit/$', views.TableUpdateView.as_view(), name='table_edit'),
    url(r'^tables/(?P<pk>\d+)/delete/$', views.TableDeleteView.as_view(), name='table_delete'),
    url(r'^tables/(?P<pk>\d+)/customers/create/$', views.CustomerCreateView.as_view(), name='customer_create'),
    url(r'^customers/(?P<pk>\d+)/detail/$', views.CustomerDetailView.as_view(), name='customer_detail'),
]
