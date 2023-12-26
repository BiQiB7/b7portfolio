from django.urls import path

from . import views

urlpatterns = [
    path('mythical_creature/', views.index, name='mythical_creature'),
]