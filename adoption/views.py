from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Pet, AdoptionRequest
from .serializers import PetSerializer, AdoptionRequestSerializer
from .permissions import IsAdminOrReadOnly, IsAuthenticated, IsAdminOrOwner


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



class AdoptionRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AdoptionRequestSerializer
    permission_classes = [IsAdminOrOwner]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return AdoptionRequest.objects.all()

        return AdoptionRequest.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
