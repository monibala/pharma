from django.urls import path
from order import views
urlpatterns = [
    path('order/', views.order, name='order'),
    path('orderdetail/<id>', views.orderdetail, name='orderdetail'),
    path('show_wishlist/',views.show_wishlist, name='show_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('removewishitems/<int:id>', views.removewishitems, name='removewishitems'),
    path('paymentdone/', views.paymentdone, name='paymentdone'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
