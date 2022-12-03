from django.urls import path
from category import views
urlpatterns = [
    path('category/<slug:slug>', views.category, name='category'),
    # path('subcategory/<slug:subcategory>', views.subcategory, name='subcategory'),
    path('subsubcategory/<str:name>', views.subsubcategory, name='subsubcategory'),
    
]
