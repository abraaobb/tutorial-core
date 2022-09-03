from django.db import models


# Create your models here.
class Book(models.Model):
    class Status(models.TextChoices):
        NEW = ('N', 'New')
        USED = ('U', 'Used')

    id = models.AutoField(
        primary_key=True
    )
    title = models.CharField(
        max_length=128,
        null=False
    )
    publication_date = models.DateField(
        null=False
    )
    author = models.CharField(
        max_length=128,
        null=False
    )
    status = models.CharField(
        max_length=1,
        null=False,
        choices=Status.choices,
        default=Status.NEW
    )

    class Meta:
        db_table = 'book'
        managed = True
