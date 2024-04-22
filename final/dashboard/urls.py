from django.urls import path
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('home.html', views.dashboard_home, name='dashboard_home'),
    path('about/', views.about, name='about'), 
    path('property-grid.html/', views.property, name='property'),
    path('property-single.html/', views.propertysingle, name='propertysingle'),
    path('blog-grid.html/', views.blog, name='blog'),
    path('blog-single.html/', views.singleblog, name='singleblog'),
    path('hotelowner.html/', views.hotelowner, name='hotelowner'),
    # path('home/', views.customer, name='customer'),
    # path('employee/', views.hotelowner, name='employee'),
]
