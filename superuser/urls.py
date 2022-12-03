from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.index, name="dashboardindex"),
    path('logout',views.Logout, name="dashboardlogout"),
    path('related/<slug:appname>/<slug:modelname>/<slug:objectid>/<slug:relatedfield>/',views.relatedmodel, name="relatedmodel"),
    path('<slug:appname>/',views.showmodels, name="showapp"),
    path('<slug:appname>/<slug:modelname>/',views.showObject, name="showdatamodel"),
    path('<slug:appname>/<slug:modelname>/<slug:objectid>/<slug:opration>/',views.editmodel, name="editdatamodel"),
    path('logindashboard',views.logindashboard,name="logindashboard"),
    path('forgotpwd', views.forgotpwd, name='forgotpwd'),
    path('pwdchange/<str:id>', views.pwd_reset_change, name='pwdchange'),
    path('changepwd', views.changepwd, name='changepwd'),
]