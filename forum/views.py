from rest_framework import generics
from .models import Section
from .serializers import SectionSerializer


class SectionApiView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
