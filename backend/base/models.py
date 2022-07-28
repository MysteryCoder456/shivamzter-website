from enum import Enum
from django.db import models


class PageChoices(Enum):
    Simplista = "Simplista"
    Roundista = "Roundista"
    Stylizta = "Stylizta"


class RoadmapItem(models.Model):
    page = models.TextField(
        choices=[(choice.name, choice.value) for choice in PageChoices]
    )
    block_name = models.CharField(null=False, max_length=100)
    block_id = models.IntegerField(null=False)
    alt_names = models.CharField(null=True, max_length=100)
    thumbnail = models.ImageField(null=False)
    # TODO: Carousel images...
