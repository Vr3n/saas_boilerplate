from django.contrib import admin

from saas_boilerplate.organisations.models import Organisation

# Register your models here.


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
