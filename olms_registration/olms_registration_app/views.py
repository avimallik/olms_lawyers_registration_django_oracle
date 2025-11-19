from django.shortcuts import render, redirect
from .forms import TestForm
from .models import TBL_TEST
from django.db import connection
from .models import Lawyer
from .models import Division, Country, BarAssociation, Area, Branch, Lawyer
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
def insert_name(request):
    msg = ""

    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            TBL_TEST.objects.create(name=form.cleaned_data["name"])
            msg = "Data Inserted Successfully!"
    else:
        form = TestForm()

    return render(request, "insert.html", {"form": form, "msg": msg})


def register(request):

    divisions = Division.objects.all()
    countries = Country.objects.all()
    bar_associations = BarAssociation.objects.all()

    if request.method == "POST":
        name_eng = request.POST.get("name_english")

        with connection.cursor() as cur:
            cur.execute("""
                INSERT INTO LAWYERS (NAME_ENGLISH)
                VALUES (:1)
            """, [name_eng])

        messages.success(request, "Successfully Registered.")
        return redirect("register")

    return render(request, "register.html", {
        "divisions": divisions,
        "countries": countries,
        "bar_associations": bar_associations
    })


def get_areas(request, division_id):
    areas = Area.objects.filter(division_id=division_id).values(
        "area_id", "area_name", "area_code"
    )
    return JsonResponse(list(areas), safe=False)


def get_branches(request, division_id, area_id):
    branches = Branch.objects.filter(
        division_id=division_id,
        area_id=area_id
    ).values("branch_id", "branch_name", "branch_code")

    return JsonResponse(list(branches), safe=False)
