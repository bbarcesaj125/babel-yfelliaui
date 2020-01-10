from django.db import models
from django.utils.html import format_html
from .utils import get_century
from django.utils.translation import gettext as _

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name=_("Prénom")
    )
    last_name = models.CharField(max_length=30, verbose_name=_("Nom"))
    name = models.CharField(max_length=61, null=True, editable=False)
    century_birth = models.IntegerField(
        blank=True, null=True, editable=False, verbose_name=_("Siècle")
    )
    date_birth = models.DateField(
        blank=True, null=True, verbose_name=_("Date de naissance")
    )
    place_birth = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Lieu de naissance")
    )

    date_died = models.DateField(blank=True, null=True, verbose_name=_("Date de décès"))
    place_died = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Lieu de décès")
    )

    content = models.TextField(blank=True, null=True, verbose_name=_("Contenu"))
    image_url = models.URLField(blank=True, null=True, verbose_name=_("Url de l'image"))
    image_file = models.ImageField(blank=True, null=True, verbose_name=_("Image"))

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.last_name

    def clean(self):
        """ Calculating birth century and putting the author's fullname into the field `name` """

        get_century(self)

        if self.first_name:
            self.name = f"{self.first_name} {self.last_name}"
        else:
            self.name = self.last_name


class Dewey(models.Model):
    name = models.CharField(max_length=61, verbose_name=_("Nom"))
    number = models.CharField(max_length=3, verbose_name=_("Numéro"))
    bg_color = models.CharField(max_length=7, default="*", editable=False)
    text_color = models.CharField(max_length=7, default="*", editable=False)

    BG_COLOR_CHOICES = [
        ("#000000", "black"),  # Black 000
        ("#8B4513", "maroon"),  # Maroon 100
        ("#FF0000", "red"),  # Red 200
        ("#FF4500", "orange"),  # Orange 300
        ("#FFFF00", "yellow"),  # Yellow 400
        ("#32CD32", "green"),  # Green 500
        ("#1E90FF", "blue"),  # Blue 600
        ("#8B008B", "purple"),  # Purple 700
        ("#A9A9A9", "grey"),  # Grey 800
        ("#FFFFFF", "white"),  # White 900
    ]
    TEXT_COLOR_CHOICES = [
        ("#FFFFFF", "black"),
        ("#000000", "white"),
    ]

    def __str__(self):
        return f"{self.number} {self.name}"

    def clean(self):
        str_number = str(int(self.number))
        if len(str_number) < 3:
            str_number = str(int(self.number))
            if len(str_number) < 2:
                str_number = "00" + str_number
            else:
                str_number = "0" + str_number
        self.number = str_number

    def colored_number(self):
        for i in range(0, len(self.BG_COLOR_CHOICES)):
            if str(self.number)[:1] == str(i):
                print("0******************")
                self.bg_color = self.BG_COLOR_CHOICES[i][0]
            if str(self.number)[:1] == "0":
                self.text_color = self.TEXT_COLOR_CHOICES[0][0]
            if str(self.number)[:1] == "9":
                self.text_color = self.TEXT_COLOR_CHOICES[1][0]

        return format_html(
            '<span style="background-color: {}; color: {}; display: inline-block; min-width: 50px;">{}</span>',
            self.bg_color,
            self.text_color,
            self.number,
        )


class Publication(models.Model):
    TYPEPUBLICATION_CHOICES = [
        ("*", "Autre"),
        ("B", "Livre"),
        ("M", "Musique"),
        ("F", "Film"),
    ]

    name = models.CharField(max_length=61, verbose_name=_("Nom"))
    reference = models.CharField(
        max_length=61, editable=False, verbose_name=_("Référence")
    )
    type_publication = models.CharField(
        max_length=1,
        choices=TYPEPUBLICATION_CHOICES,
        default="B",
        verbose_name=_("Type de publication"),
    )
    genre = models.CharField(max_length=35, verbose_name=_("Genre"))
    ISBN = models.CharField(max_length=50, blank=True, null=True)

    author = models.ForeignKey(
        Author, models.PROTECT, null=True, verbose_name=_("Autheur")
    )
    dewey_number = models.ForeignKey(
        Dewey, models.PROTECT, null=True, verbose_name=_("Numéro Dewey")
    )

    date_publication = models.DateField(
        blank=True, null=True, verbose_name=_("Date de publication")
    )
    label_editor = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Editeur")
    )
    nb_tracks_page = models.IntegerField(
        blank=True, null=True, verbose_name=_("Nombre de pages")
    )
    content = models.TextField(blank=True, null=True, verbose_name=_("Contenu"))
    image_url = models.URLField(blank=True, null=True, verbose_name=_("Url de l'image"))
    image_file = models.ImageField(blank=True, null=True, verbose_name=_("Image"))

    class Meta:
        ordering = ["reference"]

    def __str__(self):
        return f"{self.reference} {self.name}"

    def clean(self):
        if self.dewey_number and self.author:
            self.reference = f"{self.dewey_number.number}.{self.author.last_name[:3].upper()}.{self.pk}"
        else:
            self.reference = f"WAITING.{self.pk}"
