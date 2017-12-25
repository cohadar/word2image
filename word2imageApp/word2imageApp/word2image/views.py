from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Word2image
from .serializers import word2imageSerializer


def index(request):
    context = {}
    return render(request, 'index.html', context)


def prepare_data(request):
    context = {}
    return render(request, 'prepareData.html', context)


def research_images(request):
    context = {}
    return render(request, 'researchData.html', context)


# word2image/
class prepareData(APIView):
    def get(self, request):
        db_data = Word2image.get_next_for_updating()
        if db_data:
            result = word2imageSerializer(db_data, many=True)
            if result and len(result.data) > 0:
                return Response(result.data[0])
        return Response({}, status=status.HTTP_404_NOT_FOUND)
