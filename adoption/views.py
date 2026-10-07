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

    def perform_update(self, serializer):
        adoption_request = self.get_object()

        # Only admin can change approval status
        if not self.request.user.is_staff:
            serializer.save(
                status=adoption_request.status
            )
            return

        updated_request = serializer.save()

        # If admin approves the request,
        # mark the pet as adopted.
        if updated_request.status == AdoptionRequest.Status.APPROVED:
            updated_request.pet.status = Pet.Status.ADOPTED
            updated_request.pet.save(update_fields=["status"])
