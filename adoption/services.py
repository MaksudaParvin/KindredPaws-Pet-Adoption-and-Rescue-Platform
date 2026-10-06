from django.core.exceptions import ValidationError

from .models import Pet, AdoptionRequest


def validate_adoption_request(user, pet):
    """
    Validate whether a user can submit an adoption request
    for the given pet.
    """

    # Rule 1: Pet must be available
    if pet.status != Pet.Status.AVAILABLE:
        raise ValidationError(
            "This pet is no longer available for adoption."
        )

    # Rule 2: User cannot have another active request
    active_request_exists = AdoptionRequest.objects.filter(
        user=user,
        pet=pet,
        status__in=[
            AdoptionRequest.Status.PENDING,
            AdoptionRequest.Status.APPROVED,
        ],
    ).exists()

    if active_request_exists:
        raise ValidationError(
            "You already have an active adoption request "
            "for this pet."
        )