from django.contrib import admin
# Register your models here.
from models import User, UserCV, CV, Company, CompanyJob, JobCategory, JobDeliver, JobWanted, Manage


class UserAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name', 'sex', 'email', 'tel')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name', 'property', 'email', 'tel')


class CVAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name', 'school', 'major', 'expected_job')


class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('cate_name',)


class JobDeliverAdmin(admin.ModelAdmin):
    list_display = ('ID', 'job_name', 'salary')


class ManageAdmin(admin.ModelAdmin):
    list_display = ('ID', 'role')


class CompanyJObAdmin(admin.ModelAdmin):
    list_display = ('ID', 'company_id', 'job_deliver_id')


class UserCVAdmin(admin.ModelAdmin):
    list_display = ('ID', 'user_id', 'cv_id')


class JobWantedAdmin(admin.ModelAdmin):
    list_display = ('ID', 'result')


admin.site.register(Company, CompanyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Manage, ManageAdmin)
admin.site.register(UserCV, UserCVAdmin)
admin.site.register(CV, CVAdmin)
admin.site.register(JobDeliver, JobDeliverAdmin)
admin.site.register(JobWanted, JobWantedAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(CompanyJob, CompanyJObAdmin)
