from django.contrib import admin
from django.forms import Textarea
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

from places.models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = [
        'image_file', 'image_preview', 'index',
    ]
    readonly_fields = [
        'image_preview',
    ]

    def image_preview(self, obj):
        preview_image_height = 200
        return format_html('<img src="{0}" height={1} />', obj.image_file.url, preview_image_height)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (
        ImageInline,
    )
