from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Web.models import Hostels
from json import loads

@api_view(['GET'])
def index(request):
    context = {}
    return render(request, 'index.html', context)

@api_view(['POST'])
def registerHostel(request):
    hostelRecord = Hostels(name=request.DATA['name'],contactNo = request.DATA['contact'],
    rating = request.DATA['rating'],
    address = loads(request.DATA['address']))
    hostelRecord.save()
    return Response({"data": hostelRecord.id}, 200)