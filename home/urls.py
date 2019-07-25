from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.HomeView.as_view(),name='home')
]
