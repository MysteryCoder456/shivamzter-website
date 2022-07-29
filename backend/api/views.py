from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import RoadmapItem
from .serializers import RoadmapItemSerializer


@api_view(["GET"])
def get_roadmap_data(request: HttpRequest):
    print(request.GET.dict())

    if len(request.GET):
        items = RoadmapItem.objects.filter(**request.GET.dict())
    else:
        items = RoadmapItem.objects.all()

    serializer = RoadmapItemSerializer(items, many=True)
    return Response(serializer.data)
