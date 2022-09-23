from rest_framework import viewsets
from .models import Section, Theme, Comment
from .serializers import SectionSerializer, ThemeSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
def get_themes(request, section_id):
    themes = Theme.objects.filter(section_id=section_id).all()
    serializer = ThemeSerializer(themes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_comments(request, theme_id):
    comments = Comment.objects.filter(theme_id=theme_id).all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
