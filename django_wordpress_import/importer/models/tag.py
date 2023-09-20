from django.db import models

from .abstract import WordpressModel, field_max_length


class WPTag(WordpressModel):
    """Model definition for Tags."""

    SOURCE_URL = "/wp-json/wp/v2/tags"
    UNIQUE_FIELDS = ["name"]
    # TODO side effect of this is that it will not update the tag if it already exists

    name = models.CharField(
        max_length=field_max_length,
    )
    count = models.IntegerField(
        default=0,
    )
    link = models.URLField(
        max_length=field_max_length,
    )
    slug = models.SlugField(
        max_length=field_max_length,
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=field_max_length,
    )
    taxonomy = models.CharField(
        max_length=field_max_length,
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
