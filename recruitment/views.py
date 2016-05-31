# coding=utf-8
from django.shortcuts import render
from forms import LoginForm
from models import *
# Create your views here.


def home(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ID_number = cd['ID_number']
            pwd = cd['password']
            print "获得用户输入学号和密码"
            print ID_number
            print pwd
            try:
                print "查询数据库中是否存在该用户..."
                try:  # 查询应聘者是否存在该用户
                    login_data = User.objects.get(ID=ID_number)
                except:  # 查询企业是否存在该用户
                    login_data = Company.objects.get(ID=ID_number)
                print "用户查询成功,数据库中存在该用户"
                manage_data = Manage.objects.get(ID=login_data.mid)
                if pwd != manage_data.password:
                    print "密码错误"
                    return render(request, 'index.html', {'form': form, 'warning_message': "密码错误"})
                if manage_data.role == '0':  # 登录用户为应聘者
                    details = [login_data.name, login_data.sex, login_data.email, login_data.tel]
                    all_cv_data = UserCV.objects.all().filter(user_id=ID_number)  # 获得该招聘者的对应的所有cv_id
                    cvs = []
                    for cv_data in all_cv_data:
                        cvs.append(CV.objects.get(ID=cv_data.cv_id))
                    return render(request, 'index.html', {'user_role': '应聘者', 'details': details, 'cvs': cvs})
                elif manage_data.role == '1':  # 登录用户为发布者
                    details = [login_data.name, login_data.address, login_data.establish, login_data.email, login_data.property,
                               login_data.tel, login_data.intro]
                    all_com_del_data = CompanyJob.objects.all().filter(company_id=ID_number)  # 在company_job表 获得该公司发布的招聘信息的job_deliver_id
                    job_delivers = []  # 该企业发布的招聘需求，以及该招聘下投的简历
                    for job_deliver_data in all_com_del_data:
                        deliver = JobDeliver.objects.get(ID=job_deliver_data.job_deliver_id)  # 发布的详细信息
                        cv_ids = JobWanted.objects.all().filter(job_deliver=deliver.ID)
                        deliver_cvs = []  # 每个招聘对应的简历
                        for cv_id in cv_ids:
                            deliver_cvs.append(CV.objects.get(ID=cv_id.cv_id))

                        job_delivers.append([deliver, deliver_cvs])
                    return render(request, 'index.html', {'user_role': '企业', 'details': details, 'job_delivers': job_delivers})
            except:
                print "该用户不存在"
                return render(request, 'index.html', {'form': form, 'warning_message': "数据库不存在此用户"})

    return render(request, 'index.html', {'form': form})

