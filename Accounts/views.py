from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from Accounts.models import Admin
from Accounts.serializers import AdminSerializer, AdminLoginSerializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminLoginViewSet(generics.CreateAPIView):
    serializer_class = AdminLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        try:
            admin = Admin.objects.get(username=username)
        except Admin.DoesNotExist:
            return Response({"detail": "Admin not found."}, status=status.HTTP_404_NOT_FOUND)

        if admin.password != password:
            return Response({"detail": "password incorrect"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        admin_serializer = AdminSerializer(admin)

        # Return success response if the code is valid
        return Response({
            'admin': admin_serializer.data,
            'message': "login successfully"
        }, status=status.HTTP_200_OK)
