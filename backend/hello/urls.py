from django.urls import path
from .views import *
from rest_framework.routers import *


urlpatterns = [
    path('hello/', HelloApiView.as_view(), name="hello-endpoint" )
]