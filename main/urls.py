from django.urls import path
from . import views

urlpatterns = [
    path('', views.home1),
    path('category/<int:pk>', views.categ),
    path('theme/<int:pk>', views.categ),
    path('theme2/<int:pk>', views.theme2),
]