from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserViewSet(GenericViewSet):

    pagination_class = PageNumberPagination
    permission_classes = (UserPermission,)
    serializer_class = UserSerializer

    def retrieve(self, request, pk):

        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):

        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):

        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





