from rest_framework import serializers
from base.models import RoadmapItem, RoadmapCarouselImage


class RoadmapCarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapCarouselImage
        fields = ["id", "image"]


class RoadmapItemSerializer(serializers.ModelSerializer):
    carousel_images = serializers.SerializerMethodField()

    def get_carousel_images(self, obj):
        return RoadmapCarouselImageSerializer(
            obj.carousel_images, many=True
        ).data

    class Meta:
        model = RoadmapItem
        fields = "__all__"
