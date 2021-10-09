from django.urls import path
from . import views

urlpatterns = [
    path('' or 'index', views.index,name='home'),
    path('add',views.add,name='add'),
]