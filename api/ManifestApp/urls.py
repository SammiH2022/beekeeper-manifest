from django.urls import include, path
from rest_framework import routers
from . import views, models

router = routers.DefaultRouter()
router.register(r'nodes', views.NodeViewSet, basename="nodes")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]