from django.urls import path 
from .views import home,create,download_zip


urlpatterns = [
    path('',home,name='home'),
    path('create',create,name='create'),
    path('download_zip/', download_zip, name='download_zip'),
]
