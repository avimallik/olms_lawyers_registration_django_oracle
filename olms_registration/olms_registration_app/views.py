import json
from django.shortcuts import render, redirect
from .forms import TestForm
from .models import TBL_TEST
from django.db import connection
from .models import Lawyer
from .models import Division, Country, BarAssociation, Area, Branch, Lawyer, TypeOfApplication, TypeOfPost
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

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

# @csrf_exempt
# def api_register(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "POST method required"}, status=400)

    try:
        body = json.loads(request.body.decode('utf-8'))

        # --------- Extract IDs ---------
        division_id = body.get("division_id")
        area_id = body.get("area_id")
        branch_id = body.get("branch_id")

        # --------- Lookup models ---------
        div = Division.objects.get(division_id=division_id)
        area = Area.objects.get(area_id=area_id)
        branch = Branch.objects.get(branch_id=branch_id)

        # --------- Build Data ---------
        data = {
            "branch_name": branch.branch_name,
            "branch_code": branch.branch_code,

            "area_name": area.area_name,
            "area_code": area.area_code,

            "division_name": div.division_name,
            "division_code": div.division_code,

            "country": body.get("country"),

            "name_english": body.get("name_english"),
            "name_bangla": body.get("name_bangla"),

            "bar_council_passing_year": body.get("bar_council_passing_year"),
            "bar_council_certificate_no": body.get("bar_council_certificate_no"),
            "year_permission_practice_high_court": body.get("year_permission_practice_high_court"),

            "bar_association_membership_no": body.get("bar_association_membership_no"),
            "member_of_bar_association": body.get("member_of_bar_association"),

            "bar_at_law": body.get("bar_at_law"),

            "address_present_english": body.get("address_present_english"),
            "address_present_bangla": body.get("address_present_bangla"),

            "address_permanent_english": body.get("address_permanent_english"),
            "address_permanent_bangla": body.get("address_permanent_bangla"),

            "address_court_chamber_english": body.get("address_court_chamber_english"),
            "address_court_chamber_bangla": body.get("address_court_chamber_bangla"),

            "address_personal_chamber_english": body.get("address_personal_chamber_english"),
            "address_personal_chamber_bangla": body.get("address_personal_chamber_bangla"),

            "email": body.get("email"),
            "mobile": body.get("mobile"),
            "nid": body.get("nid"),

            "experiences": body.get("experiences"),
            "other_academic_qualifications": body.get("other_academic_qualifications"),

            "passport_no": body.get("passport_no"),
            "passport_expiry_date": body.get("passport_expiry_date"),

            "overseas_national_id": body.get("overseas_national_id"),
            "diploma_or_professional_degree": body.get("diploma_or_professional_degree"),

            "other_training": body.get("other_training"),
            "date_of_birth": body.get("date_of_birth"),

            "highest_education": body.get("highest_education"),

            "codice_fiscale": body.get("codice_fiscale"),

            "document_ho_inward_no": body.get("document_ho_inward_no"),

            "type_of_application": body.get("type_of_application"),
            "application_session": body.get("application_session"),
            "type_of_post": body.get("type_of_post"),
        }

        # --------- INSERT INTO DATABASE ---------
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
                    TYPE_OF_APPLICATION,
                    APPLICATION_SESSION,
                    TYPE_OF_POST
                )
                VALUES (
                    %(branch_name)s, %(branch_code)s,
                    %(area_name)s, %(area_code)s,
                    %(division_name)s, %(division_code)s,
                    %(country)s,

                    %(name_english)s, %(name_bangla)s,

                    %(bar_council_passing_year)s, %(bar_council_certificate_no)s,
                    %(year_permission_practice_high_court)s,

                    %(bar_association_membership_no)s,
                    %(member_of_bar_association)s,
                    %(bar_at_law)s,

                    %(address_present_english)s, %(address_present_bangla)s,
                    %(address_permanent_english)s, %(address_permanent_bangla)s,
                    %(address_court_chamber_english)s, %(address_court_chamber_bangla)s,
                    %(address_personal_chamber_english)s, %(address_personal_chamber_bangla)s,

                    %(email)s, %(mobile)s, %(nid)s,
                    %(experiences)s, %(other_academic_qualifications)s,

                    %(passport_no)s,
                    TO_DATE(%(passport_expiry_date)s, 'YYYY-MM-DD'),

                    %(overseas_national_id)s,
                    %(diploma_or_professional_degree)s,

                    %(other_training)s,
                    TO_DATE(%(date_of_birth)s, 'YYYY-MM-DD'),

                    %(highest_education)s,
                    %(codice_fiscale)s,
                    %(document_ho_inward_no)s,

                    %(type_of_application)s,
                    TO_DATE(%(application_session)s, 'YYYY-MM-DD'),
                    %(type_of_post)s
                )
            """, data)

        return JsonResponse({"success": True, "message": "Registration Completed Successfully!"})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)
    
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

@csrf_exempt
def api_register(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "POST required"})

    try:
        body = request.POST

        photo = request.FILES.get("photo_filename")

        photo_path = ""
        if photo:
            from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage(location="media/uploads/")
            filename = fs.save(photo.name, photo)
            photo_path = fs.url(filename)

        # IDs
        division_id = body.get("division_id")
        area_id = body.get("area_id")
        branch_id = body.get("branch_id")

        div = Division.objects.get(division_id=division_id)
        area = Area.objects.get(area_id=area_id)
        branch = Branch.objects.get(branch_id=branch_id)

        # Build data dict
        data = {
            "branch_name": branch.branch_name,
            "branch_code": branch.branch_code,
            "area_name": area.area_name,
            "area_code": area.area_code,
            "division_name": div.division_name,
            "division_code": div.division_code,

            "country": body.get("country"),
            "name_english": body.get("name_english"),
            "name_bangla": body.get("name_bangla"),

            "bar_council_passing_year": body.get("bar_council_passing_year"),
            "bar_council_certificate_no": body.get("bar_council_certificate_no"),
            "year_permission_practice_high_court": body.get("year_permission_practice_high_court"),

            "bar_association_membership_no": body.get("bar_association_membership_no"),
            "member_of_bar_association": body.get("member_of_bar_association"),

            "bar_at_law": body.get("bar_at_law"),

            "address_present_english": body.get("address_present_english"),
            "address_present_bangla": body.get("address_present_bangla"),

            "address_permanent_english": body.get("address_permanent_english"),
            "address_permanent_bangla": body.get("address_permanent_bangla"),

            "address_court_chamber_english": body.get("address_court_chamber_english"),
            "address_court_chamber_bangla": body.get("address_court_chamber_bangla"),

            "address_personal_chamber_english": body.get("address_personal_chamber_english"),
            "address_personal_chamber_bangla": body.get("address_personal_chamber_bangla"),

            "email": body.get("email"),
            "mobile": body.get("mobile"),
            "nid": body.get("nid"),

            "experiences": body.get("experiences"),
            "other_academic_qualifications": body.get("other_academic_qualifications"),

            "passport_no": body.get("passport_no"),
            "passport_expiry_date": body.get("passport_expiry_date"),

            "overseas_national_id": body.get("overseas_national_id"),
            "diploma_or_professional_degree": body.get("diploma_or_professional_degree"),

            "other_training": body.get("other_training"),
            "date_of_birth": body.get("date_of_birth"),

            "highest_education": body.get("highest_education"),
            "codice_fiscale": body.get("codice_fiscale"),
            "document_ho_inward_no": body.get("document_ho_inward_no"),

            "type_of_application": body.get("type_of_application"),
            "application_session": body.get("application_session"),
            "type_of_post": body.get("type_of_post"),

            "photo_filename": photo_path,  # FIXED
        }

        # Insert same as before...
        with connection.cursor() as cur:
            cur.execute("""
                INSERT INTO TBL_LAYWER_REGISTER (
                    BRANCH_NAME, BRANCH_CODE, AREA_NAME, AREA_CODE,
                    DIVISION_NAME, DIVISION_CODE, COUNTRY,
                    NAME_ENGLISH, NAME_BANGLA,
                    BAR_COUNCIL_PASSING_YEAR, BAR_COUNCIL_CERTIFICATE_NO,
                    YEAR_PERMISSION_PRACTICE_HIGH_COURT,
                    BAR_ASSOCIATION_MEMBERSHIP_NO, MEMBER_OF_BAR_ASSOCIATION,
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
                    HIGHEST_EDUCATION, CODICE_FISCALE, DOCUMENT_HO_INWARD_NO,
                    TYPE_OF_APPLICATION, APPLICATION_SESSION,
                    TYPE_OF_POST, PHOTO_FILENAME
                )
                VALUES (
                    :branch_name, :branch_code, :area_name, :area_code,
                    :division_name, :division_code, :country,
                    :name_english, :name_bangla,
                    :bar_council_passing_year, :bar_council_certificate_no,
                    :year_permission_practice_high_court,
                    :bar_association_membership_no, :member_of_bar_association,
                    :bar_at_law,
                    :address_present_english, :address_present_bangla,
                    :address_permanent_english, :address_permanent_bangla,
                    :address_court_chamber_english, :address_court_chamber_bangla,
                    :address_personal_chamber_english, :address_personal_chamber_bangla,
                    :email, :mobile, :nid,
                    :experiences, :other_academic_qualifications,
                    :passport_no,
                    TO_DATE(:passport_expiry_date, 'YYYY-MM-DD'),
                    :overseas_national_id, :diploma_or_professional_degree,
                    :other_training,
                    TO_DATE(:date_of_birth, 'YYYY-MM-DD'),
                    :highest_education, :codice_fiscale, :document_ho_inward_no,
                    :type_of_application,
                    TO_DATE(:application_session, 'YYYY-MM-DD'),
                    :type_of_post, :photo_filename
                )
            """, data)

        return JsonResponse({"success": True})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})

def register(request):

    if request.method == "POST":

        # Build final validated values using DB lookups
        division_id = request.POST.get("division")
        area_id = request.POST.get("area")
        branch_id = request.POST.get("branch")

        div = Division.objects.get(division_id=division_id)
        area = Area.objects.get(area_id=area_id)
        branch = Branch.objects.get(branch_id=branch_id)

        photo = request.FILES.get("photo")
        photo_path = ""

        if photo:
            from django.core.files.storage import FileSystemStorage
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            photo_path = fs.url(filename)

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
            "type_of_post": request.POST.get("type_of_post"),
            "photo_filename": photo_path,
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

                    TYPE_OF_APPLICATION, APPLICATION_SESSION, TYPE_OF_POST, PHOTO_FILENAME
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
                    :email, 
                    :mobile, 
                    :nid,
                    :experiences, :other_academic_qualifications,
                    :passport_no, 
                    TO_DATE(:passport_expiry_date, 'YYYY-MM-DD'),
                    :overseas_national_id, 
                    :diploma_or_professional_degree,
                    :other_training, 
                    TO_DATE(:date_of_birth, 'YYYY-MM-DD'),
                    :highest_education,
                    :codice_fiscale,
                    :document_ho_inward_no,
                    :type_of_application,
                    TO_DATE(:application_session, 'YYYY-MM-DD'),
                    :type_of_post,
                    :photo_filename
                )
            """, data)

        messages.success(request, "Registration Completed Successfully!")
        return redirect("register")

    # GET request
    divisions = Division.objects.all()
    countries = Country.objects.all()
    bar_associations = BarAssociation.objects.all()
    application_type = TypeOfApplication.objects.all()
    post_type = TypeOfPost.objects.all()

    return render(request, "register.html", {
        "divisions": divisions,
        "countries": countries,
        "bar_associations": bar_associations,
        "application_type": application_type,
        "post_type": post_type,
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

def get_division(request):
    divisions = Division.objects.all().values(
        'division_id', 
        'division_name', 
        'division_code'
    )

    return JsonResponse({
        "status": "success",
        "divisions": list(divisions)
    }, safe=False)

def get_country(request):
    country = Country.objects.all().values(
        'id',
        'name_country',
    )

    return JsonResponse({
        "status": "success",
        "country": list(country)
    }, safe=False)

def get_member_bar_association(request):
    memberOfBarAssociation = BarAssociation.objects.all().values(
        'id',
        'name_member_of_bar_association',
    )

    return JsonResponse({
        "status": "success",
        "member_of_bar_association": list(memberOfBarAssociation)
    }, safe=False)

def get_type_of_application(request):
    typeOfApplication = TypeOfApplication.objects.all().values(
        'id', 
        'status', 
        'application_type'
    )

    return JsonResponse({
        "status": "success",
        "type_of_application": list(typeOfApplication)
    }, safe=False)

def get_type_of_post(request):
    typeOfPost = TypeOfPost.objects.all().values(
        'id',
        'post_type'
    )

    return JsonResponse({
        'status': 'success',
        'type_of_post': list(typeOfPost)
    }, safe=False)

def get_areas(request, division_id):
    data = list(Area.objects.filter(division_id=division_id)
                .values("area_id", "area_name", "area_code"))
    return JsonResponse(data, safe=False)


def get_branches(request, division_id, area_id):
    data = list(Branch.objects.filter(division_id=division_id, area_id=area_id)
                .values("branch_id", "branch_name", "branch_code"))
    return JsonResponse(data, safe=False)

