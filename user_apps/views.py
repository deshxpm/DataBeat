from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework import viewsets, status
from rest_framework import generics
from .models import *

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors, 'message': 'Something went wrong!'})
        serializer.save()
        
        user_obj = UserProfile.objects.get(username=serializer.data['username'])
        print(user_obj,1212545)
        token_obj , _ = Token.objects.get_or_create(user=user_obj)

        return Response({'status': 201, 'data': serializer.data, 'token': str(token_obj)})

# class CreateMovie(generics.ListCreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     serializer_class = MoviesSerializer

#     def get_queryset(self):
#         return Movies.objects.all()

#     def perform_create(self, serializer):
#         serializer = MoviesSerializer(data=self.request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication] # Authentication by JWT
    permission_classes = [IsAuthenticated]
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def get_queryset(self):
        try:
            return Movies.objects.all()
        except Movies.DoesNotExist as e:
            return Response({'status': 404, 'error':"movie does't exist"})


    
class CastViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

    def get_queryset(self):
        try:
            return Cast.objects.all()
        except Cast.DoesNotExist as e:
            return Response({'status': 404, 'error':"cast does't exist"})
# class CreateCast(generics.ListCreateAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     serializer_class = CastSerializer

#     def get_queryset(self):
#         return Cast.objects.all()

#     def perform_create(self, serializer):
#         serializer = CastSerializer(data=self.request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
