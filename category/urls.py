from django.urls import path
from category import views
urlpatterns = [
    path('category/<slug:slug>', views.category, name='category'),
    path('subcategory/<slug:slug>', views.subcategory, name='subcategory'),
    path('subsubcategory/<slug:slug>', views.subsubcategory, name='subsubcategory'),
    
]
