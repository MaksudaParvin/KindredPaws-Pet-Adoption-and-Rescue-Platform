from rest_framework import serializers

from .models import Pet, AdoptionRequest


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "animal_type",
            "breed",
            "age",
            "gender",
            "location",
            "description",
            "image",
            "status",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]



class AdoptionRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdoptionRequest
        fields = [
            "id",
            "user",
            "pet",
            "phone",
            "address",
            "reason",
            "previous_pet_experience",
            "message",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "user",
            "status",
            "created_at",
        ]

    def validate(self, attrs):
        pet = attrs["pet"]
        user = self.context["request"].user

        # Rule 1: Pet must be available
        if pet.status != Pet.Status.AVAILABLE:
            raise serializers.ValidationError(
                {"pet": "This pet is not available for adoption."}
            )

        # Rule 2: User cannot have multiple active requests
        active_requests = AdoptionRequest.objects.filter(
            user=user,
            pet=pet,
            status__in=[
                AdoptionRequest.Status.PENDING,
                AdoptionRequest.Status.APPROVED,
            ],
        )

        if active_requests.exists():
            raise serializers.ValidationError(
                {"pet": "You already have an active adoption request for this pet."}
            )

        return attrs