from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    # path('index',auth_views.LogoutView.as_view(next_page='index'),name='logout',),
    path('policy/', views.policy, name='policy'),
    path('uploadprescription/', views.uploadprescription,name='uploadprescription'),
    path('search', views.search, name='search'),
    path('logout/', views.logout_view, name='logout'),
]
