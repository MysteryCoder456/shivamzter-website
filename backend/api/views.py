from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import RoadmapItem
from .serializers import RoadmapItemSerializer


@api_view(["GET"])
def get_data(request):
    items = RoadmapItem.objects.all()
    serializer = RoadmapItemSerializer(items, many=True)
    return Response(serializer.data)
