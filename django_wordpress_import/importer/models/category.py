from django.db import models

from .abstract import WordpressModel, field_max_length


class WPCategory(WordpressModel):
    """Model definition for Category."""

    SOURCE_URL = "/wp-json/wp/v2/categories"

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
    )
    taxonomy = models.CharField(
        max_length=field_max_length,
    )
    parent = models.ForeignKey(
        "importer.WPCategory",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    @staticmethod
    def process_foreign_keys():
        """These are excluded from the first import and processed later."""
        return [
            {
                "parent": {"model": "self", "field": "wp_id"},
            }
        ]
