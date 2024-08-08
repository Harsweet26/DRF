from django.shortcuts import render
from .models import*
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Itemserializer


# Create your views here.

class CreateItem(APIView):
    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')
        item = Item(
            name = name,
            description = description,
            price = price,
        )
        item.save()
        
        resp = {
            'resultcode': '1',
            'result': 'your record has been inserted successfully'
        }
        
        return Response(resp)
    
    
    def get(self,request):
        qs = Item.objects.all()
        serializer = Itemserializer(qs, many=True)
        result = serializer.data
        return Response(result)
    
# http://127.0.0.1:8000/product/create-product/
