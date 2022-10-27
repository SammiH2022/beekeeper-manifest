from django.contrib.auth.models import *
from .models import *
from rest_framework.generics import ListCreateAPIView
from .api.serializers import NodeSerializer


class NodeList(ListCreateAPIView):

    queryset = NodeData.objects.all().order_by("VSN")
    serializer_class = NodeSerializer