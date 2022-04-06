from django.urls import path

from .views import *

urlpatterns = [
    path("int:pk/", DetailNewton.as_view()),
    path('', ListNewton.as_view()),
]