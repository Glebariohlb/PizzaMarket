from django.urls import path
from pizzashop import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('home/', views.index, name='home'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
]