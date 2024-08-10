from django.urls import path

from saas_boilerplate.organisations.views import create_organisation_view, organisation_list_view


urlpatterns = [
    path('', organisation_list_view, name="list"),
    path('create/', create_organisation_view, name="create"),
]
