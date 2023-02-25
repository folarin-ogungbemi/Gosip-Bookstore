from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False)
    book_title = models.CharField(
        max_length=100,
        null=False,
        blank=False)
    about = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Special(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


RATING = [
    (1, 'very bad'),
    (2, 'bad'),
    (3, 'okay'),
    (4, 'good'),
    (5, 'excellent'),
]


class Books(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=260, unique=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='book')
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='book_category')
    special = models.ManyToManyField(
        Special,
        blank=True)
    publication_year = models.IntegerField()
    pages = models.IntegerField()
    language = models.CharField(max_length=100)
    isbn = models.IntegerField(unique=True)
    dimension = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)])
    rating = models.PositiveIntegerField(
        choices=RATING,
        null=True,
        blank=True)
    description = models.TextField(
        null=False,
        blank=False
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Books, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} by {self.author}"
