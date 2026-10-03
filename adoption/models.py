from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator


class Pet(models.Model):

    class AnimalType(models.TextChoices):
        DOG = "Dog", "Dog"
        CAT = "Cat", "Cat"
        BIRD = "Bird", "Bird"
        RABBIT = "Rabbit", "Rabbit"
        OTHER = "Other", "Other"

    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    class Status(models.TextChoices):
        AVAILABLE = "Available", "Available"
        ADOPTED = "Adopted", "Adopted"

    name = models.CharField(max_length=100)

    animal_type = models.CharField(
        max_length=20,
        choices=AnimalType.choices
    )

    breed = models.CharField(max_length=100)

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices
    )

    location = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(
        upload_to="pets/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AdoptionRequest(models.Model):

    class Status(models.TextChoices):
        PENDING = "Pending", "Pending"
        APPROVED = "Approved", "Approved"
        REJECTED = "Rejected", "Rejected"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="adoption_requests"
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name="adoption_requests"
    )

    phone = models.CharField(max_length=20)

    address = models.TextField()

    reason = models.TextField()

    previous_pet_experience = models.BooleanField(
        default=False
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.pet.name}"