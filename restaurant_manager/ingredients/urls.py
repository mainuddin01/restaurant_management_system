from django.conf.urls import url

from . import views

app_name = 'ingredients'

urlpatterns = [
    url(r'^$', views.IngredientListView.as_view(), name='list'),
    url(r'^create/$', views.IngredientCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/detail$', views.IngredientDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.IngredientUpdateView.as_view(), name='edit'),
    url(r'^categories/$', views.IngredientCategoryListView.as_view(), name='category_list'),
    url(r'^categories/create/$', views.IngredientCategoryCreateView.as_view(), name='create_category'),
    url(r'^categories/(?P<slug>[\w-]+)/$', views.IngredientCategoryDetailView.as_view(), name='category_detail'),
    url(r'^categories/(?P<slug>[\w-]+)/edit/$', views.IngredientCategoryUpdateView.as_view(), name='edit_category'),
]
