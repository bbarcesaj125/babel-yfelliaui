from django.contrib import admin
from .models import Author, Publication, Dewey


class PublicationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "reference",
        "type_publication",
        "genre",
        "author",
        "dewey_number",
        "date_publication",
        "label_editor",
        "nb_tracks_page",
        "content",
        "image_url",
        "image_file",
    )

    fieldsets = (
        ("Reference", {"fields": ("type_publication", "dewey_number", "reference",)},),
        ("Publication", {"fields": ("name", "isbn", "author",)},),
        (
            "General options",
            {
                "classes": ("collapse",),
                "fields": (
                    "date_publication",
                    "label_editor",
                    "nb_tracks_page",
                    "content",
                    "image_url",
                    "image_file",
                ),
            },
        ),
    )

    radio_fields = {"type_publication": admin.HORIZONTAL}
    readonly_fields = ("reference",)


class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        "last_name",
        "first_name",
        "date_birth",
    )


class DeweyAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "name",
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)


# Register your models here.
