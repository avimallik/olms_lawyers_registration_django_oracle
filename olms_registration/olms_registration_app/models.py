from django.db import models

# Create your models here.

class TBL_TEST(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "TBL_TEST"

class Division(models.Model):
    division_id = models.IntegerField(primary_key=True)
    division_name = models.CharField(max_length=100)
    division_code = models.CharField(max_length=50)

    class Meta:
        db_table = "TBL_DIVISION"
        managed = False


class Area(models.Model):
    area_id = models.IntegerField(primary_key=True)
    division_id = models.IntegerField()
    area_name = models.CharField(max_length=100)
    area_code = models.CharField(max_length=50)

    class Meta:
        db_table = "TBL_AREA"
        managed = False


class Branch(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    division_id = models.IntegerField()
    area_id = models.IntegerField()
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=50)

    class Meta:
        db_table = "TBL_BRANCH"
        managed = False



class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name_country = models.CharField(max_length=200)

    class Meta:
        db_table = "TBL_COUNTRY"
        managed = False


class BarAssociation(models.Model):
    id = models.IntegerField(primary_key=True)
    name_member_of_bar_association = models.CharField(max_length=200)

    class Meta:
        db_table = "TBL_MEMBER_OF_BAR_ASSOCIATION"
        managed = False

class TypeOfApplication(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=200)
    application_type = models.CharField(max_length=200)

    class Meta:
        db_table = "TBL_TYPE_OF_APPLICATION"
        managed = False

class Lawyer(models.Model):
    id = models.AutoField(primary_key=True)

    division = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    country = models.CharField(max_length=100)
    member_of_bar_association = models.CharField(max_length=200)

    name_english = models.CharField(max_length=200)
    name_bangla = models.CharField(max_length=200, null=True, blank=True)

    bar_council_passing_year = models.CharField(max_length=10, null=True, blank=True)
    bar_council_certificate_no = models.CharField(max_length=50, null=True, blank=True)
    year_permission_practice_high_court = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "LAWYERS"
        managed = False 