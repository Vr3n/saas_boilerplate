from django.db import models
from saas_boilerplate.utils.models import BaseModel

# Create your models here.


class Organisation(BaseModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE,
        related_name="owned_organisations",
        null=True
    )
    admins = models.ManyToManyField(
        "users.User", related_name="admin_in_organisations", blank=True,
        null=True
    )
    members = models.ManyToManyField("users.User",
                                     related_name="organisations",
                                     blank=True)

    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="organisations/logos/",
                             blank=True,
                             null=True)

    def all_members(self):
        """
        returns all members including owner and admins.
        """
        return self.members.all() | self.members.all() | self.owner

    def __str__(self) -> str:
        return self.name
