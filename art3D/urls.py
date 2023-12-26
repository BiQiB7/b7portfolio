from django.urls import path

from . import views

urlpatterns = [
    path('art3D/', views.index, name='art3D'),
]