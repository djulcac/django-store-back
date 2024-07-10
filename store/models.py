import uuid

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from . import validators

# Create your models here.
class Base(models.Model):
    key = models.UUIDField(
        default = uuid.uuid4,
        editable = False,
        unique=True,
        null=False,
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        editable = False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable = False,
    )
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Companies(Base):
    business_name = models.CharField(max_length=255)
    registration_name = models.CharField(max_length=255)
    ruc = models.BigIntegerField(
        unique=True,
        validators=[validators.validate_eleven_digits],
    )
    website = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.business_name}'


class Categories(Base):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
    )

    def __str__(self):
        return f'{self.id} {self.name}'


class Products(Base):
    company = models.ForeignKey(
        Companies,
        on_delete=models.CASCADE,
    )
    categories = models.ManyToManyField(
        Categories,
        blank=True,
    )
    business_name = models.CharField(max_length=255)
    registration_name = models.CharField(max_length=255)
    gtin_type = models.CharField(
        max_length=7,
        choices=(
            ('EAN8','EAN8'),
            ('EAN13','EAN13'),
            ('LOCAL','LOCAL'),
        ),
        default='EAN13',
    )
    gtin = models.BigIntegerField()
    # Global Trade Item Number

    def clean(self):
        super().clean()
        if self.gtin_type == 'EAN13' and not len(str(self.gtin)) == 13:
            raise ValidationError({'gtin': f'With {self.gtin_type}, gtin must have lenght 13.'})
        elif self.gtin_type == 'EAN8' and not len(str(self.gtin)) == 8:
            raise ValidationError({'gtin': f'With {self.gtin_type}, gtin must have lenght 8.'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        unique_together = [
            ('gtin_type', 'gtin'),
        ]

    def __str__(self):
        return f'{self.id} {self.business_name}'
