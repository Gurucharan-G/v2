from django.shortcuts import render,redirect
from .models import doctor_register
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

# Create your views here.
def doctor_signup(request):
    if request.method=='POST':
        Name=request.POST['Name']
        gender=request.POST['gender']
        number=request.POST['number']
        address=request.POST['address']
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password=password)
        user.save()
        docs =doctor_register(Name=Name,gender=gender,number=number,address=address,username=username,password=password)
        docs.save()
        print('saved')
        return redirect('/')
    else:
        return render(request,'doc_sinup.html')

def doctor_log(request):
    if request.method=='POST':
        username_1=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username_1,password=password)
        if user is not None:
            a=doctor_register.objects.all().filter(username=username_1)
            for c in a:
                if c.username==username_1:
                    cc=c.Name
                    print(cc)
            auth.login(request,user)
            return render(request,'docindex.html',{"cc":cc})
        else:
            return redirect('/doctor_sinup')
    else: return render(request,'doc_log.html')