from django.urls import path
from .views import index

urlpatterns = [
    path("fs/", index, name="index")
]
