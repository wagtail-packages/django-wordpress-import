from rest_framework import serializers

from django_wordpress_import.importer.models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = WPAuthor
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = WPTag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WPCategory
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = WPPost
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WPComment
        fields = "__all__"


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WPPage
        fields = "__all__"


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WPMedia
        fields = "__all__"
