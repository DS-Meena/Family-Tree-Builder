from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('create/parent/<str:pk>', views.create_parent, name='create_parent'),
    # path('create/offspring', views.create_offspring, name='create_offspring'),
]
