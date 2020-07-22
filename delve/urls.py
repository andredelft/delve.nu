from django.urls import path
from django.views.generic import RedirectView

from delve import views

urlpatterns = [
    path('', views.home, name = 'home')
]
