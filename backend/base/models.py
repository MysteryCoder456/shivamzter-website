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
    block_name = models.CharField(null=False, blank=False, max_length=100)
    block_id = models.IntegerField(null=False, blank=False)
    alt_names = models.CharField(null=True, blank=True, max_length=100)
    thumbnail = models.ImageField(
        null=False, blank=False, upload_to="roadmap-thumbnails"
    )

    def __str__(self):
        return f'RoadmapItem<id={self.id} block_id={self.block_id} block_name="{self.block_name}">'  # type: ignore


class RoadmapCarouselImage(models.Model):
    image = models.ImageField(null=False, upload_to="roadmap-carousel")
    roadmap_item = models.ForeignKey(
        RoadmapItem, on_delete=models.CASCADE, related_name="carousel_images"
    )

    def __str__(self):
        return f"RoadmapCarouselImage<id={self.id} roadmap_item_id={self.roadmap_item.id}>"  # type: ignore
