from django.urls import path
from .views import find_paths

urlpatterns = [
    path('paths', find_paths, name='find_paths'),
]
