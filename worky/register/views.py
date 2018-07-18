import jwt,json
from rest_framework import views
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status, exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from .models import Register

class Login(views.APIView):

    def post(self, request, *args, **kwargs):
        token = None
        if not request.data:
            return Response({'Error': "Ups! Necesitas el name y description."}, status="400")
        
        try:
            name = request.data['name']
            description = request.data['description']
        except:
            return Response({'Error': "Ups! Datos incorrectos."}, status="400")
            
        try:
            register = Register.objects.create(name=name, description=description)

            payload = {
                'name': name,
                'description': description
            }

            token = jwt.encode(payload, "Worky_2018").decode("utf-8")

        except:
            register = Register.objects.get(name=name, description=description)
            token = register.token
            
        return Response({'token':  token}, status=200)
