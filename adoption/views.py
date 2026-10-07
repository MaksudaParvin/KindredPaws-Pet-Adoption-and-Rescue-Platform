from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Pet, AdoptionRequest
from .serializers import PetSerializer, AdoptionRequestSerializer
from .permissions import IsAdminOrReadOnly, IsAuthenticated, IsAdminOrOwner

from django.db import transaction


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

    @transaction.atomic
    def perform_update(self, serializer):
        adoption_request = self.get_object()

        # Only admin can change the adoption request status
        if not self.request.user.is_staff:
            serializer.save(
                status=adoption_request.status
            )
            return

        updated_request = serializer.save()

        # If the request is approved
        if updated_request.status == AdoptionRequest.Status.APPROVED:

            pet = updated_request.pet

            # Mark the pet as adopted
            pet.status = Pet.Status.ADOPTED
            pet.save(update_fields=["status"])

            # Reject all other pending requests for this pet
            AdoptionRequest.objects.filter(
                pet=pet,
                status=AdoptionRequest.Status.PENDING
            ).exclude(
                id=updated_request.id
            ).update(
                status=AdoptionRequest.Status.REJECTED
            )

