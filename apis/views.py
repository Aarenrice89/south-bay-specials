from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apis.serializers import RegisterNewUserSerializer


@api_view(("GET",))
def ping(request):
    return Response({"data": "pong"})


@extend_schema(
    methods=["POST"],
    request=RegisterNewUserSerializer,
    responses={201: inline_serializer("Successful registration", fields={"detail": "User registered successfully"})},
)
@api_view(("POST",))
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterNewUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create(serializer.validated_data)
        return Response({"detail": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
