from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Pet
from .serializers import PetSerializer
from .permissions import IsAdminOrReadOnly


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        "name",
        "breed",
        "animal_type",
        "location",
    ]

    filterset_fields = [
        "animal_type",
        "gender",
        "location",
        "status",
    ]

    ordering_fields = [
        "name",
        "age",
        "created_at",
    ]

    ordering = ["-created_at"]
