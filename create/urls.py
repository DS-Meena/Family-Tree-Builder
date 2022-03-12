from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('create/relation/', views.create_relation, name='create_relation'),
    # path('create/parent/<str:pk>', views.create_parent, name='create_parent'),
]
