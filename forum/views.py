from rest_framework import generics
from .models import Section, Theme, Comment
from .serializers import SectionSerializer, ThemeSerializer, CommentSerializer


class SectionApiView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class SectionApiViewRU(generics.RetrieveUpdateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class ThemeApiView(generics.ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class ThemeApiViewRU(generics.RetrieveUpdateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class CommentApiView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentApiViewRU(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
