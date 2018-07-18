import jwt,json
from rest_framework import views
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status, exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from .models import Register

class TokenAuthentication(BaseAuthentication):
    model = None

    def get_model(self):
        return Register

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'token':
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token=="null":
                msg = 'Null token not allowed'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        register = self.get_model()
        msg = {'Error': "Token mismatch",'status' :"401"}

        try:
            payload = jwt.decode(token, "Worky_2018")
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed(msg)

        name = payload['name']
        description = payload['description']
        try:
            register = Register.objects.filter(
                name=name,
                description=description
            ).first()
            
            if register.token != token.decode("utf-8"):
                raise exceptions.AuthenticationFailed(msg)
               
        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return HttpResponse({'Error': "Token is invalid"}, status="403")
        except register.DoesNotExist:
            return HttpResponse({'Error': "Internal server error"}, status="500")

        return (register, token)

    def authenticate_header(self, request):
        return 'Token'