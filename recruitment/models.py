from django.db import models


# Create your models here.
class Manage(models.Model):
    ID = models.CharField(max_length=12, primary_key=True)
    role = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.ID


class Company(models.Model):
    ID = models.CharField(max_length=11, primary_key=True)
    mid = models.ForeignKey(Manage)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    establish = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    property = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    scale = models.CharField(max_length=20)
    intro = models.TextField(max_length=300)

    def __unicode__(self):
        return self.ID


class JobCategory(models.Model):
    cate_name = models.CharField(max_length=20, primary_key=True)
    pre_cate = models.CharField(max_length=20)

    def __unicode__(self):
        return self.cate_name


class JobDeliver(models.Model):
    ID = models.CharField(max_length=11, primary_key=True)
    category = models.ForeignKey(JobCategory)
    job_name = models.CharField(max_length=20)
    position = models.CharField(max_length=40)
    numb = models.IntegerField()
    sex = models.CharField(max_length=10)
    work_year = models.CharField(max_length=5)
    age = models.CharField(max_length=10)
    education = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    contact = models.CharField(max_length=20)
    created_time = models.CharField(max_length=20)

    def __unicode__(self):
        return self.ID


class CompanyJob(models.Model):
    ID = models.CharField(max_length=11, primary_key=True)
    company = models.ForeignKey(Company)
    job_deliver = models.ForeignKey(JobDeliver)

    def __unicode__(self):
        return self.ID


class CV(models.Model):
    ID = models.CharField(max_length=11, primary_key=True)
    category = models.ForeignKey(JobCategory)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    birth = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    education = models.CharField(max_length=20)
    work_exp = models.CharField(max_length=100)
    school = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    intro = models.TextField(max_length=300)
    expected_job = models.CharField(max_length=20)

    def __unicode__(self):
        return self.ID


class User(models.Model):
    ID = models.CharField(max_length=11, primary_key=True)
    mid = models.ForeignKey(Manage)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)

    def __unicode__(self):
        return self.ID


class UserCV(models.Model):
    ID = models.CharField(max_length=11, primary_key=True)
    user = models.ForeignKey(User)
    cv = models.ForeignKey(CV)

    def __unicode__(self):
        return self.ID


class JobWanted(models.Model):
    ID = models.CharField(max_length=11, primary_key=True)
    result = models.CharField(max_length=10)
    job_deliver = models.ForeignKey(JobDeliver)
    cv = models.ForeignKey(CV)

    def __unicode__(self):
        return self.ID
