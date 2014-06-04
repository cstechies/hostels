from django.shortcuts import render
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    context = {}
    return render(request, 'index.html', context)