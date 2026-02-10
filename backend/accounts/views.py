from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,LoginSerializer,User_serializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    return Response(serializer.data,status = status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user=serializer.validated_data['user']

    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    
    data = {
        "refresh": str(refresh),
        "access": str(access),
    }

    return Response(data,status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def user_view(request):
    serializer = User_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data,status=status.HTTP_200_OK)