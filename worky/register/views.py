import jwt
from rest_framework import views
from rest_framework.response import Response
from .models import Register


class Login(views.APIView):

    def get_model(self):
        return Register

    def post(self, request, *args, **kwargs):
        """
        Get or crete jwt with name and description.
        :param request: HTTP request
        :return: Authentication token
        """
        token = None
        register = self.get_model()

        if not request.data:
            return Response({'Error': "Ups! Necesitas el name y description."}, status="400")
        
        try:
            name = request.data['name']
            description = request.data['description']
        except KeyError:
            return Response({'Error': "Ups! Datos incorrectos."}, status="400")
            
        try:
            register = Register.objects.create(name=name, description=description)

            payload = {
                'name': name,
                'description': description
            }

            token = jwt.encode(payload, "Worky_2018").decode("utf-8")

        except Exception:
            register = Register.objects.get(name=name, description=description)
            token = register.token
            
        return Response({'token':  token}, status=200)
