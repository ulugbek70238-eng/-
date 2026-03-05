from django.urls import path
from . import views

urlpatterns = [
    path('', views.home1, name='home'),
    path('category/<int:pk>/', views.categ),
    path('theme/<int:pk>/', views.categ),
    path('theme2/<int:pk>', views.theme2),
    path('register/', views.Register.as_view(), name='register'),
    path('search', views.search, name='search'),
    path('logout/', views.logout_view, name='logout'),
    path('add-favorite/<int:pk>/', views.add_favorite, name='add_favorite'),
    path('cart/', views.cart_page, name='cart'),
    path('remove-favorite/<int:pk>/', views.remove_favorite, name='remove_favorite'),
]