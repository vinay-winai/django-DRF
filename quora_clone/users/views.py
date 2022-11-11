from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EndUserSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework import permissions

# login view with JWT token generation

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            serializer = AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)
            response =  super().post(request, format=None)
            if response.status_code>=400:
                return Response({
                    "message": "Incorrect credentials"
                },status=401)
            if response.status_code==200:
                response.status_code=201
            return response
        except Exception as e:
            return Response({
                "message": "Incorrect credentials"
            },status=401)

# register endpoint view

@api_view(http_method_names=["POST"])
def register(request):
    try:
        serializer = EndUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message" : "User is registered successfully"
        }, status=201)
    except Exception as e:
        return Response({
            "message":e.__str__()
        },status=400)