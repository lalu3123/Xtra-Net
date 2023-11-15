from django.shortcuts import render,redirect
from .models import data_Tab,Support_Engineer_tab,Issue_Tab,Status_Tab,ESCALATION_Tab

# Create your views here.
def use_Home(request):
    data = data_Tab.objects.all()
    Support_Engineer_ = Support_Engineer_tab.objects.all()
    Issue_=Issue_Tab.objects.all()
    Status_=Status_Tab.objects.all()
    ESCALATION_=ESCALATION_Tab.objects.all()
    for i in data:
        print(i.Support_Engineer)
    OUT={"data_":data,"Support_Engineer_":Support_Engineer_,"Issue_":Issue_,"Status_":Status_,"ESCALATION_":ESCALATION_}
    return render(request, "main.html",OUT)
def submit_data(request):
    if request.method == "POST":
        Support_Engineer=request.POST['Support Engineer']
        User_name=request.POST.get('User name')
        Phone_Number=request.POST.get('Phone Number')
        LCO=request.POST.get('LCO')
        Issue_=request.POST['Issue_']
        Remark=request.POST.get('Remark')
        Status=request.POST['Statuss']
        ESCALATION=request.POST['ESCALATION']
        ESCALATION_REMARK=request.POST.get('ESCALATION REMARK')
        data_Tab.objects.create(Support_Engineer=Support_Engineer, User_name=User_name,
                                phone_no=Phone_Number, LCO=LCO,Issue=Issue_,Remark=Remark,Status=Status,ESCALATION=ESCALATION,ESCALATION_REMARK=ESCALATION_REMARK)
        print(Status)
    return redirect("use_Home")

