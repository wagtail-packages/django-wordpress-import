from django.db import models

from .abstract import WordpressModel, field_max_length


class WPAuthor(WordpressModel):
    """Model definition for Author. AKA User."""

    SOURCE_URL = "/wp-json/wp/v2/users"

    name = models.CharField(
        max_length=field_max_length,
    )
    url = models.URLField(
        blank=True,
        null=True,
        max_length=field_max_length,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    link = models.URLField(
        max_length=field_max_length,
    )
    slug = models.SlugField(
        max_length=field_max_length,
    )
    avatar_urls = models.URLField(blank=True, null=True, max_length=field_max_length)  # comes from avatar_urls.96

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name
