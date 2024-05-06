from django.http import JsonResponse, HttpResponse
from .models import Good, Tokens
from uuid import uuid4
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GoodsSerializer
from rest_framework.decorators import api_view

# Create your views here.
def get_token(request):
    token = uuid4()
    new_token = Tokens(token=token)
    new_token.save()
    return JsonResponse({'token': token})

@api_view(['GET'])
def view_goods(request):
        token = request.GET.get('token')
        if not token or token == '':
            return HttpResponse('Token must be present', status=401)
        if not Tokens.objects.filter(token=token).exists():
            return HttpResponse('Token is invalid', status=401)
        
        goods = Good.objects.all()
        serializer = GoodsSerializer(goods, many=True)
        return Response(serializer.data)

class Goods_api(APIView):

    def get(self, request):
        token = request.GET.get('token')
        if not token or token == '':
            return HttpResponse('Token must be present', status=401)
        if not Tokens.objects.filter(token=token).exists():
            return HttpResponse('Token is invalid', status=401)
        return Response(token)
    
    def post(self, request):        
        new_good = GoodsSerializer(data=request.data)
        if new_good.is_valid():
            new_good.save()
            return HttpResponse("Success<br>New Good id: " + str(new_good.instance.id))
        else:
            return Response(new_good.errors, status=400)