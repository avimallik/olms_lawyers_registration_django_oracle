from django.shortcuts import render, redirect
from .forms import TestForm
from .models import TBL_TEST
from django.db import connection
from .models import Lawyer
from .models import Division, Country, BarAssociation, Area, Branch, Lawyer, TypeOfApplication
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


# def register(request):

#     divisions = Division.objects.all()
#     countries = Country.objects.all()
#     bar_associations = BarAssociation.objects.all()
#     application_type = TypeOfApplication.objects.all()

#     if request.method == "POST":
#         name_eng = request.POST.get("name_english")

#         with connection.cursor() as cur:
#             cur.execute("""
#                 INSERT INTO LAWYERS (NAME_ENGLISH)
#                 VALUES (:1)
#             """, [name_eng])

#         messages.success(request, "Successfully Registered.")
#         return redirect("register")

#     return render(request, "register.html", {
#         "divisions": divisions,
#         "countries": countries,
#         "bar_associations": bar_associations,
#         "application_type": application_type,
#     })

# def register(request):
    print("TYPE_OF_APPLICATION =", request.POST.get("type_of_application"))
    if request.method == "POST":

        data = {

            "branch_name": request.POST.get("branch"),
            "branch_code": request.POST.get("branch_code"),

            "area_name": request.POST.get("area"),
            "area_code": request.POST.get("area_code"),

            "division_name": request.POST.get("division"),
            "division_code": request.POST.get("division_code"),

            "country": request.POST.get("country"),

            "name_english": request.POST.get("name_english"),
            "name_bangla": request.POST.get("name_bangla"),

            "bar_council_passing_year": request.POST.get("bar_council_passing_year"),
            "bar_council_certificate_no": request.POST.get("bar_council_certificate_no"),
            "year_permission_practice_high_court": request.POST.get("year_permission_practice_high_court"),
            "year_permission_practice_appellate": request.POST.get("year_permission_practice_appellate"),

            "bar_association_membership_no": request.POST.get("bar_association_membership_no"),
            "member_of_bar_association": request.POST.get("member_of_bar_association"),

            "bar_at_law": request.POST.get("bar_at_law"),

            "address_present_english": request.POST.get("address_present_english"),
            "address_present_bangla": request.POST.get("address_present_bangla"),

            "address_permanent_english": request.POST.get("address_permanent_english"),
            "address_permanent_bangla": request.POST.get("address_permanent_bangla"),

            "address_court_chamber_english": request.POST.get("address_court_chamber_english"),
            "address_court_chamber_bangla": request.POST.get("address_court_chamber_bangla"),

            "address_personal_chamber_english": request.POST.get("address_personal_chamber_english"),
            "address_personal_chamber_bangla": request.POST.get("address_personal_chamber_bangla"),

            "email": request.POST.get("email"),
            "mobile": request.POST.get("mobile"),
            "nid": request.POST.get("nid"),

            "experiences": request.POST.get("experiences"),
            "other_academic_qualifications": request.POST.get("other_academic_qualifications"),

            "passport_no": request.POST.get("passport_no"),
            "passport_expiry_date": request.POST.get("passport_expiry_date"),

            "overseas_national_id": request.POST.get("overseas_national_id"),
            "diploma_or_professional_degree": request.POST.get("diploma_or_professional_degree"),

            "other_training": request.POST.get("other_training"),
            "date_of_birth": request.POST.get("date_of_birth"),

            "highest_education": request.POST.get("highest_education"),
            "photo_filename": request.POST.get("photo_filename"),

            "codice_fiscale": request.POST.get("codice_fiscale"),

            "document_branch_inward_no": request.POST.get("document_branch_inward_no"),
            "document_ho_inward_no": request.POST.get("document_ho_inward_no"),

            "type_of_application": request.POST.get("type_of_application"),
            "application_session": request.POST.get("application_session"),
        }

        with connection.cursor() as cur:
            cur.execute("""
                INSERT INTO TBL_LAYWER_REGISTER (

                    BRANCH_NAME, BRANCH_CODE,
                    AREA_NAME, AREA_CODE,
                    DIVISION_NAME, DIVISION_CODE,
                    COUNTRY,
                    NAME_ENGLISH, NAME_BANGLA,
                    BAR_COUNCIL_PASSING_YEAR, BAR_COUNCIL_CERTIFICATE_NO,
                    YEAR_PERMISSION_PRACTICE_HIGH_COURT,
                    YEAR_PERMISSION_PRACTICE_APPELLATE,
                    BAR_ASSOCIATION_MEMBERSHIP_NO,
                    MEMBER_OF_BAR_ASSOCIATION,
                    BAR_AT_LAW,
                    ADDRESS_PRESENT_ENGLISH, ADDRESS_PRESENT_BANGLA,
                    ADDRESS_PERMANENT_ENGLISH, ADDRESS_PERMANENT_BANGLA,
                    ADDRESS_COURT_CHAMBER_ENGLISH, ADDRESS_COURT_CHAMBER_BANGLA,
                    ADDRESS_PERSONAL_CHAMBER_ENGLISH, ADDRESS_PERSONAL_CHAMBER_BANGLA,
                    EMAIL, MOBILE, NID,
                    EXPERIENCES, OTHER_ACADEMIC_QUALIFICATIONS,
                    PASSPORT_NO, PASSPORT_EXPIRY_DATE,
                    OVERSEAS_NATIONAL_ID, DIPLOMA_OR_PROFESSIONAL_DEGREE,
                    OTHER_TRAINING, DATE_OF_BIRTH,
                    HIGHEST_EDUCATION, PHOTO_FILENAME,
                    CODICE_FISCALE, DOCUMENT_BRANCH_INWARD_NO,
                    DOCUMENT_HO_INWARD_NO,
                    TYPE_OF_APPLICATION, APPLICATION_SESSION
                )
                VALUES (
                    :branch_name, :branch_code,
                    :area_name, :area_code,
                    :division_name, :division_code,
                    :country,
                    :name_english, :name_bangla,
                    :bar_council_passing_year, :bar_council_certificate_no,
                    :year_permission_practice_high_court,
                    :year_permission_practice_appellate,
                    :bar_association_membership_no,
                    :member_of_bar_association,
                    :bar_at_law,
                    :address_present_english, :address_present_bangla,
                    :address_permanent_english, :address_permanent_bangla,
                    :address_court_chamber_english, :address_court_chamber_bangla,
                    :address_personal_chamber_english, :address_personal_chamber_bangla,
                    :email, :mobile, :nid,
                    :experiences, :other_academic_qualifications,
                    :passport_no, TO_DATE(:passport_expiry_date,'YYYY-MM-DD'),
                    :overseas_national_id, :diploma_or_professional_degree,
                    :other_training, TO_DATE(:date_of_birth,'YYYY-MM-DD'),
                    :highest_education, :photo_filename,
                    :codice_fiscale, :document_branch_inward_no,
                    :document_ho_inward_no,
                    :type_of_application, TO_DATE(:application_session,'YYYY-MM-DD')
                )
            """, data)

        messages.success(request, "Registration Completed Successfully!")
        return redirect("register")


    # GET request → dropdown data load
    divisions = Division.objects.all()
    countries = Country.objects.all()
    bar_associations = BarAssociation.objects.all()
    application_type = TypeOfApplication.objects.all()
    

    return render(request, "register.html", {
        "divisions": divisions,
        "countries": countries,
        "bar_associations": bar_associations,
        "application_type": application_type
    })

def register(request):

    if request.method == "POST":

        # Build final validated values using DB lookups
        division_id = request.POST.get("division")
        area_id = request.POST.get("area")
        branch_id = request.POST.get("branch")

        div = Division.objects.get(division_id=division_id)
        area = Area.objects.get(area_id=area_id)
        branch = Branch.objects.get(branch_id=branch_id)

        data = {
            "branch_name": branch.branch_name,
            "branch_code": branch.branch_code,

            "area_name": area.area_name,
            "area_code": area.area_code,

            "division_name": div.division_name,
            "division_code": div.division_code,

            "country": request.POST.get("country"),

            "name_english": request.POST.get("name_english"),
            "name_bangla": request.POST.get("name_bangla"),

            "bar_council_passing_year": request.POST.get("bar_council_passing_year"),
            "bar_council_certificate_no": request.POST.get("bar_council_certificate_no"),
            "year_permission_practice_high_court": request.POST.get("year_permission_practice_high_court"),

            "bar_association_membership_no": request.POST.get("bar_association_membership_no"),
            "member_of_bar_association": request.POST.get("member_of_bar_association"),

            "bar_at_law": request.POST.get("bar_at_law"),

            "address_present_english": request.POST.get("address_present_english"),
            "address_present_bangla": request.POST.get("address_present_bangla"),

            "address_permanent_english": request.POST.get("address_permanent_english"),
            "address_permanent_bangla": request.POST.get("address_permanent_bangla"),

            "address_court_chamber_english": request.POST.get("address_court_chamber_english"),
            "address_court_chamber_bangla": request.POST.get("address_court_chamber_bangla"),

            "address_personal_chamber_english": request.POST.get("address_personal_chamber_english"),
            "address_personal_chamber_bangla": request.POST.get("address_personal_chamber_bangla"),

            "email": request.POST.get("email"),
            "mobile": request.POST.get("mobile"),
            "nid": request.POST.get("nid"),

            "experiences": request.POST.get("experiences"),
            "other_academic_qualifications": request.POST.get("other_academic_qualifications"),

            "passport_no": request.POST.get("passport_no"),
            "passport_expiry_date": request.POST.get("passport_expiry_date"),

            "overseas_national_id": request.POST.get("overseas_national_id"),
            "diploma_or_professional_degree": request.POST.get("diploma_or_professional_degree"),

            "other_training": request.POST.get("other_training"),
            "date_of_birth": request.POST.get("date_of_birth"),

            "highest_education": request.POST.get("highest_education"),

            "codice_fiscale": request.POST.get("codice_fiscale"),

            "document_ho_inward_no": request.POST.get("document_ho_inward_no"),

            "type_of_application": request.POST.get("type_of_application"),
            "application_session": request.POST.get("application_session"),
        }

        with connection.cursor() as cur:
            cur.execute("""
                INSERT INTO TBL_LAYWER_REGISTER (

                    BRANCH_NAME, BRANCH_CODE,
                    AREA_NAME, AREA_CODE,
                    DIVISION_NAME, DIVISION_CODE,
                    COUNTRY,

                    NAME_ENGLISH, NAME_BANGLA,

                    BAR_COUNCIL_PASSING_YEAR, BAR_COUNCIL_CERTIFICATE_NO,
                    YEAR_PERMISSION_PRACTICE_HIGH_COURT,

                    BAR_ASSOCIATION_MEMBERSHIP_NO,
                    MEMBER_OF_BAR_ASSOCIATION,
                    BAR_AT_LAW,

                    ADDRESS_PRESENT_ENGLISH, ADDRESS_PRESENT_BANGLA,
                    ADDRESS_PERMANENT_ENGLISH, ADDRESS_PERMANENT_BANGLA,

                    ADDRESS_COURT_CHAMBER_ENGLISH, ADDRESS_COURT_CHAMBER_BANGLA,
                    ADDRESS_PERSONAL_CHAMBER_ENGLISH, ADDRESS_PERSONAL_CHAMBER_BANGLA,

                    EMAIL, MOBILE, NID,
                    EXPERIENCES, OTHER_ACADEMIC_QUALIFICATIONS,

                    PASSPORT_NO, PASSPORT_EXPIRY_DATE,
                    OVERSEAS_NATIONAL_ID, DIPLOMA_OR_PROFESSIONAL_DEGREE,

                    OTHER_TRAINING, DATE_OF_BIRTH,

                    HIGHEST_EDUCATION,
                    CODICE_FISCALE,
                    DOCUMENT_HO_INWARD_NO,

                    TYPE_OF_APPLICATION, APPLICATION_SESSION
                )
                VALUES (
                    :branch_name, :branch_code,
                    :area_name, :area_code,
                    :division_name, :division_code,
                    :country,
                    :name_english, :name_bangla,
                    :bar_council_passing_year, :bar_council_certificate_no,
                    :year_permission_practice_high_court,
                    :bar_association_membership_no,
                    :member_of_bar_association,
                    :bar_at_law,
                    :address_present_english, :address_present_bangla,
                    :address_permanent_english, :address_permanent_bangla,
                    :address_court_chamber_english, :address_court_chamber_bangla,
                    :address_personal_chamber_english, :address_personal_chamber_bangla,
                    :email, :mobile, :nid,
                    :experiences, :other_academic_qualifications,
                    :passport_no, TO_DATE(:passport_expiry_date, 'YYYY-MM-DD'),
                    :overseas_national_id, :diploma_or_professional_degree,
                    :other_training, TO_DATE(:date_of_birth, 'YYYY-MM-DD'),
                    :highest_education,
                    :codice_fiscale,
                    :document_ho_inward_no,
                    :type_of_application,
                    TO_DATE(:application_session, 'YYYY-MM-DD')
                )
            """, data)

        messages.success(request, "Registration Completed Successfully!")
        return redirect("register")

    # GET request
    divisions = Division.objects.all()
    countries = Country.objects.all()
    bar_associations = BarAssociation.objects.all()
    application_type = TypeOfApplication.objects.all()

    return render(request, "register.html", {
        "divisions": divisions,
        "countries": countries,
        "bar_associations": bar_associations,
        "application_type": application_type
    })


# def get_areas(request, division_id):
#     areas = Area.objects.filter(division_id=division_id).values(
#         "area_id", "area_name", "area_code"
#     )
#     return JsonResponse(list(areas), safe=False)


# def get_branches(request, division_id, area_id):
    branches = Branch.objects.filter(
        division_id=division_id,
        area_id=area_id
    ).values("branch_id", "branch_name", "branch_code")

    return JsonResponse(list(branches), safe=False)


def get_areas(request, division_id):
    data = list(Area.objects.filter(division_id=division_id)
                .values("area_id", "area_name", "area_code"))
    return JsonResponse(data, safe=False)


def get_branches(request, division_id, area_id):
    data = list(Branch.objects.filter(division_id=division_id, area_id=area_id)
                .values("branch_id", "branch_name", "branch_code"))
    return JsonResponse(data, safe=False)