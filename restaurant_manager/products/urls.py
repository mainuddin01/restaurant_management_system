from django.conf.urls import url

from . import views

app_name = 'products'

urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='list'),
    url(r'^create/$', views.ProductCreateView.as_view(), name='create'),
    url(r'^image/create/$', views.ProductImageCreateView.as_view(), name='image_create'),
    url(r'^(?P<slug>[\w-]+)/$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.ProductUpdateView.as_view(), name='edit'),
    url(r'^categories/create/$', views.ProductCategoryCreateView.as_view(), name='create_category'),
]
