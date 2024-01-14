from django.shortcuts import render ,redirect
from django.http import HttpResponse
from signup.models import signup_details
from login.models import login_details

def home(request):
    return render(request,"index.html")


def signup(request):
    return render(request,"signup.html")

def signup_info(request):
    if request.method=='POST':

        email=request.POST['email']
        dob=request.POST['DOB']
        address=request.POST['address']
        desination=request.POST['desination']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password!=confirm_password:
           d={'key':"Password does not matched",'s':"*"}
           return render(request,'signup.html',d)
        else:
            user=signup_details.objects.create(email=email,DOB=dob,address=address,desination=desination,password=password,confirm_password=confirm_password)
            # return HttpResponse("you have successfully inserted your details in database")
            return ('login')
    return render(request,'signup.html')
    
def login(request):
    return render(request,"login.html")

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=signup_details.objects.get(email=email,password=password)
        if user.password==password:
            return HttpResponse("you have been login in successfully")
        else:
            return HttpResponse('Entered credential are not in record')
    return render(request,'login.html')    
    
    