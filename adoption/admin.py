from django.contrib import admin
from .models import Pet, AdoptionRequest


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "animal_type",
        "breed",
        "age",
        "gender",
        "location",
        "status",
        "created_at",
    )

    list_filter = (
        "animal_type",
        "gender",
        "status",
        "location",
    )

    search_fields = (
        "name",
        "breed",
        "location",
    )

    ordering = ("-created_at",)


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "pet",
        "phone",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "user__username",
        "pet__name",
        "phone",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "user",
        "pet",
        "phone",
        "address",
        "reason",
        "previous_pet_experience",
        "message",
        "created_at",
    )