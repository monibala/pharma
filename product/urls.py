from django.urls import path
from product import views
urlpatterns = [
    path('products/', views.products, name='products'),
    path('productsingle/<slug:slug>', views.productsingle, name='productsingle'),
    path('review/', views.review, name='review'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('delete/', views.delete, name='delete'),
    path('update/' , views.update,name='update'),
    path('account/' , views.account,name='account'),
    path('address/' , views.address,name='address'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('empty/', views.empty, name='empty'),
    path('checkpincode/', views.checkpincode, name='checkpincode'),
    path('pay/', views.pay, name='pay'),
    path('send_notification/', views.send_notification,name='send_notification'),
]
