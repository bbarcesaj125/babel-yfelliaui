from django.contrib import admin
from .models import Author, Publication, Dewey
from django.utils.translation import gettext as _


class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "reference",
        "ISBN",
        "type_publication",
        "genre",
        "author",
        "dewey_number",
        "date_publication",
        "label_editor",
    )

    list_reference = (("type_publication", "dewey_number"), ("ISBN", "reference"))
    list_publication = (
        "name",
        "author",
        "label_editor",
    )
    list_details = (
        "date_publication",
        "nb_tracks_page",
        "content",
        "image_url",
        "image_file",
    )

    fieldsets = (
        (_("Reference"), {"fields": list_reference}),
        (_("Publication"), {"fields": list_publication}),
        (_("Details"), {"classes": ("collapse",), "fields": list_details}),
    )

    radio_fields = {"type_publication": admin.HORIZONTAL}
    readonly_fields = ("reference",)
    search_fields = [
        "name",
        "reference",
        "dewey_number__number",
        "dewey_number__name",
    ]
    autocomplete_fields = [
        "author",
        "dewey_number",
    ]
    list_filter = (
        "dewey_number__number",
        "author__last_name",
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_birth", "century_birth")
    list_identity = [("last_name", "first_name",)]
    list_birth = [("date_birth", "place_birth", "century_birth",)]
    list_death = [("date_died", "place_died",)]
    list_details = [("content", "image_url", "image_file",)]

    fieldsets = (
        (_("Identité"), {"fields": list_identity}),
        (_("Naissance"), {"fields": list_birth}),
        (_("Décès"), {"classes": ("collapse",), "fields": list_death}),
        (_("Details"), {"classes": ("collapse",), "fields": list_details}),
    )
    readonly_fields = ("century_birth",)
    search_fields = (
        "first_name",
        "last_name",
    )
    list_filter = (
        "first_name",
        "last_name",
    )


class DeweyAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "name",
        "colored_number",
    )
    search_fields = [
        "name",
        "number",
    ]
    list_filter = ("name",)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Dewey, DeweyAdmin)


# Register your models here.
