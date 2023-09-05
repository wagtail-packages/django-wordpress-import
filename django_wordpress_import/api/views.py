from rest_framework import viewsets

from django_wordpress_import.api.serializers import *
from django_wordpress_import.importer.models import *


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = WPAuthor.objects.all().order_by("wp_id")
    serializer_class = AuthorSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = WPTag.objects.all().order_by("wp_id")
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = WPCategory.objects.all().order_by("wp_id")
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = WPPost.objects.all().order_by("wp_id")
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = WPComment.objects.all().order_by("wp_id")
    serializer_class = CommentSerializer


class PageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = WPPage.objects.all().order_by("wp_id")
    serializer_class = PageSerializer


class MediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = WPMedia.objects.all().order_by("wp_id")
    serializer_class = MediaSerializer
