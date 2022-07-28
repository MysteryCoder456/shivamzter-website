from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_data(request):
    card = {"block": 69420}
    return Response(card)
