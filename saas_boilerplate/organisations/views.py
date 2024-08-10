from django.shortcuts import redirect, render
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse


from saas_boilerplate.organisations.forms import OrganisationForm
from saas_boilerplate.organisations.models import Organisation


# Create your views here.

def organisation_list_view(request: HttpRequest) -> HttpResponse:
    orgs: QuerySet[Organisation] = request.user.organisations.all(
    ) | request.user.owned_organisations.all()

    context = {
        'orgs': orgs
    }
    return render(request, "organisations/organisation_list.html",
                  context=context)


def create_organisation_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form: OrganisationForm = OrganisationForm(request.POST, request.FILES)
        if form.is_valid():
            org: Organisation = form.save(commit=False)
            org.owner = request.user
            org.admins.add(request.user)
            org.save()
            return redirect("organisations:list")

    form: OrganisationForm = OrganisationForm()
    return render(
        request,
        "organisations/create_organisation.html",
        {"form": form}
    )
