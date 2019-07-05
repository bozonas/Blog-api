from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
from . import models
from . import serializers

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = serializers.UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = serializers.GroupSerializer

# class LoginView(viewsets.ModelViewSet):
#     """
#     POST auth/login/
#     """
#     # This permission class will overide the global permission
#     # class setting
#     permission_classes = (permissions.AllowAny,)

#     queryset = User.objects.all()

#     def post(self, request, *args, **kwargs):

#         return Response("OK")

# class PostDetail(viewsets.ModelViewSet):
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer

class PostViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = models.Post.objects.all()
        serializer = serializers.PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = serializers.PostSerializer(post)
        return Response(serializer.data)
