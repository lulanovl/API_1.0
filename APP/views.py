
from rest_framework import generics
from .models import Newton
from .serializers import NewtonSerializer

class ListNewton(generics.ListAPIView):
    queryset = Newton.objects.all()
    serializer_class = NewtonSerializer

class DetailNewton(generics.RetrieveAPIView):
    queryset = Newton.objects.all()
    serializer_class = NewtonSerializer