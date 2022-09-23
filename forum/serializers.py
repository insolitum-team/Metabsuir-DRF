from rest_framework import serializers
from .models import Section, Theme, Comment


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('name', )


class ThemeSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Theme
        fields = (
            'name',
            'date',
            'main_post',
            'author',
            'section',
        )


class CommentSerializer(serializers.ModelSerializer):
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = (
            'content',
            'theme',
            'reply_to',
            'sender',
            'date',
        )
