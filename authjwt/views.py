
from django.contrib.auth.models import User
from .serializers import CadasterSerializer, LoginSerializer, VerifyEmailSerializer
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class VerifyEmailView(APIView):

    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class CadasterView(APIView):
    def post(self, request):
        serializer = CadasterSerializer(data=request.data)
        
        if serializer.is_valid():
            user    = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class DeleteView(DestroyAPIView):
    queryset           = User.objects.all()
    serializer_class   = CadasterSerializer
    lookup_field       = 'id'
    permission_classes = [IsAuthenticated]

class EditView(UpdateAPIView):
    queryset           = User.objects.all()
    serializer_class   = CadasterSerializer
    lookup_field       = 'id'
    permission_classes = [IsAuthenticated]