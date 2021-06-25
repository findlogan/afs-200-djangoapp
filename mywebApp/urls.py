from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('products', views.products, name='products'),
    path('store', views.store, name='store'),
    path('userpanel', views.userpanel, name='userpanel'),
    path('logout', views.logout, name='logout'),
    path('delete/<slug:the_id>', views.delete, name='delete'),
]
