from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('prepare_data', views.prepare_data, name='prepare_data'),
    path('research_images', views.research_images, name='research_images'),
    path('prepareData', views.prepareData.as_view()),
]