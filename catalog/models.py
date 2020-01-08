from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=61, null=True, editable=False)
    century_birth = models.IntegerField(blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    place_birth = models.CharField(max_length=50, blank=True, null=True)

    date_died = models.DateField(blank=True, null=True)
    place_died = models.CharField(max_length=50, blank=True, null=True)

    content = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image_file = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.last_name


class Dewey(models.Model):
    name = models.CharField(max_length=61)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.number} {self.name}"


class Publication(models.Model):
    TYPEPUBLICATION_CHOICES = [
        ("_", "Indéfini"),
        ("B", "Livre"),
        ("M", "Musique"),
        ("F", "Film"),
    ]

    name = models.CharField(max_length=61)
    reference = models.CharField(max_length=61, editable=False)
    type_publication = models.CharField(
        max_length=1, choices=TYPEPUBLICATION_CHOICES, default="_",
    )
    genre = models.CharField(max_length=35)

    author = models.ForeignKey(Author, models.PROTECT, null=True)
    dewey_number = models.ForeignKey(Dewey, models.PROTECT, null=True)

    date_publication = models.DateField(blank=True, null=True)
    label_editor = models.CharField(max_length=50, blank=True, null=True)
    nb_tracks_page = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["reference"]

    def __str__(self):
        return f"{self.reference} {self.name}"

    def clean(self):
        if self.dewey_number and self.author:
            self.reference = f"{self.dewey_number.number}.{self.author.last_name[:3].upper()}.{self.pk}"
        else:
            self.reference = f"ENATTENTE.{self.pk}"
