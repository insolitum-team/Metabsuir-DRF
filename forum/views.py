from rest_framework import viewsets
from .models import Section, Theme, Comment
from .serializers import SectionSerializer, ThemeSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Section.objects.filter(pk=pk).all()
        return Section.objects.all()


class ThemeViewSet(viewsets.ModelViewSet):
    serializer_class = ThemeSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Theme.objects.filter(pk=pk).all()
        return Theme.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAdminOrReadOnly, IsAuthorOrReadOnly)

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Comment.objects.filter(pk=pk).all()
        return Comment.objects.all()


@api_view(['GET'])
def get_themes_by_section(request, section_id):
    themes = Theme.objects.filter(section_id=section_id).all()
    serializer = ThemeSerializer(themes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_comments_by_theme(request, theme_id):
    comments = Comment.objects.filter(theme_id=theme_id).all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
