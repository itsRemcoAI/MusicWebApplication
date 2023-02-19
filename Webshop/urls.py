from django.urls import path
from . import views

urlpatterns = [
    # http://itsremco.com/webshop/{...}
    path('index/', views.index, name='index'),
]