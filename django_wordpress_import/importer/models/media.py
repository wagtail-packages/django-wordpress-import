from django.db import models

from .abstract import WordpressModel, field_max_length


class WPMedia(WordpressModel):
    """Model definition for Media."""

    SOURCE_URL = "/wp-json/wp/v2/media"

    title = models.CharField(
        max_length=field_max_length,
    )
    date = models.DateTimeField()
    date_gmt = models.DateTimeField()
    guid = models.URLField(
        max_length=field_max_length,
    )
    modified = models.DateTimeField()
    modified_gmt = models.DateTimeField()
    slug = models.SlugField(
        max_length=field_max_length,
    )
    status = models.CharField(
        max_length=field_max_length,
    )
    comment_status = models.CharField(
        max_length=field_max_length,
    )
    ping_status = models.CharField(
        max_length=field_max_length,
    )
    type = models.CharField(
        max_length=field_max_length,
    )
    link = models.URLField(
        max_length=field_max_length,
    )
    template = models.CharField(
        max_length=field_max_length,
    )
    description = models.TextField()
    caption = models.TextField()
    alt_text = models.CharField(
        max_length=field_max_length,
    )
    media_type = models.CharField(
        max_length=field_max_length,
    )
    mime_type = models.CharField(
        max_length=field_max_length,
    )
    source_url = models.URLField(
        max_length=field_max_length,
    )
    author = models.ForeignKey(
        "importer.WPAuthor",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    post = models.ForeignKey(
        "importer.WPPost",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __str__(self):
        return self.title

    @staticmethod
    def process_fields():
        """The value is from other keys of the incoming data."""
        return [
            {"description": "description.rendered"},
            {"caption": "caption.rendered"},
            {"title": "title.rendered"},
            {"guid": "guid.rendered"},
        ]

    @staticmethod
    def process_foreign_keys():
        """These are excluded from the first import and processed later."""
        return [
            {
                "author": {"model": "WPAuthor", "field": "wp_id"},
                "post": {"model": "WPPost", "field": "wp_id"},
            }
        ]
