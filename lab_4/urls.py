from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstpage, name='firstpage'),
    path("<int:number>", views.calculate_tax, name="calculate_tax"),
    path("taxrate", views.taxrate, name="taxrate"),
]