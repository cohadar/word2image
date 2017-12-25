from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from word2image import views

urlpatterns = [
    path('word2image/', include('word2image.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
