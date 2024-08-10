from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('header/', views.header_page, name='header'),
    path('xodim_list/', views.xodim_list, name='xodim_list'),
    path('xodim_detail/<int:pk>/', views.xodim_detail, name='xodim_detail'),
    path('xodim_create/', views.xodim_create, name='xodim_create'),
    path('xodim_update/<int:pk>/', views.xodim_update, name='xodim_update'),
    path('xodim_delete/<int:pk>/', views.xodim_delete, name='xodim_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('davomat/', views.davomat, name='davomat'),
    path('profile/', views.profile, name='profile'),
    path('profile_update', views.profile_update, name='profile_update'),
]