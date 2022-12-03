from django.urls import path
from product import views
urlpatterns = [
    path('productsingle/<str:name>', views.productsingle, name='productsingle'),
    path('review/', views.review, name='review'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('delete/', views.delete, name='delete'),
    path('update/' , views.update,name='update'),
    path('account/' , views.account,name='account'),
    path('address/' , views.address,name='address'),
    path('changepassword/', views.changepassword, name='changepassword'),
]
