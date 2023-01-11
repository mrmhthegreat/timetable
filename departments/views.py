from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Department, ModelAllocationForm,AllocationForm,Course,Program, Samester_and_Section, course_and_teacher
# Create your views here.
def home(request):
    context={}
    form=ModelAllocationForm(request.POST or None)
    print(request.POST)
    cr=Course.objects.get(short_name=request.POST['courses_ids'])
    proram=Program.objects.get(short_name=request.POST['program_id'])
    sms=Samester.objects.get(short_name=request.POST['samester_id'])

    AllocationForm.objects.create(
    roll_number=request.POST['roll_number'],

    email= request.POST['email'],
    full_name = request.POST['full_name'],
    gender=request.POST['gender'],
    phone =request.POST['phone'],
    section=request.POST['section'],
    courses_ids=cr,
    program_id=proram,
    samester_id=sms,
    is_available=True
)
    

#     print(request.POST.);
   
    if form.is_valid():
        form.save()

    context['form']=form

    return render(request,'home.html',context)
def allocationform(request):
    depart=Department.objects.all()
    context={"department":depart}
    return render(request,"home.html",context)


def programs(request):

    print("depart")

    department_id=request.GET.get('department')
    depart=Program.objects.filter(department_id=department_id)
    print(depart)

    context={"program":depart}
    return render(request,"program.html",context)
def samester(request):

    print("depart")

    program_id=request.GET.get('program')
    depart=Samester_and_Section.objects.filter(program_id=program_id)
    print(depart)

    context={"samester":depart}
    return render(request,"samester.html",context)
def courser(request):

    print("depart")

    program_id=request.GET.get('section')
    depart=course_and_teacher.objects.filter(section_id=program_id)
    print(depart)

    context={"courser":depart}
    return render(request,"courser.html",context)
def courserj(request):

    print("depart")

    program_id=request.GET.get('section')
    depart=course_and_teacher.objects.filter(section_id=program_id)
    print(depart)
    data={'data':[]}
    for i in   depart:
        print(i.course_id)
        print(i.short_name)
        data['data'].append('course'+i.short_name)
    return JsonResponse(data)
def fill(request):

    print(request.POST.get)
    formdata= AllocationForm(roll_number=request.POST.get('roll','98888'),
    email= request.POST.get('email','noemai@gmail.com'),
    full_name = request.POST.get('name','nonmae'),
    section=request.POST.get('email','noemai@gmail.com'),
    program_id=request.POST.get('program','noemai@gmail.com'),
    samester_id=request.POST.get('samester','noemai@gmail.com'),
    department_id=request.POST.get('department',''),
    
    )
    formdata.courses_ids.add()

    return JsonResponse({'Done':"Dobe"})

