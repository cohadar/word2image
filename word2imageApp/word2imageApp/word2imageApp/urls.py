from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('word2image/', include('word2image.urls')),
]
