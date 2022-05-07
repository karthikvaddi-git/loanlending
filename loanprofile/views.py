from django.shortcuts import render
from django.http import HttpResponse
from .models import profilemodel
# Create your views here.
def index(request):
    return render(request,"index.html")


def filesharing(request):


    if request.method=="POST":
        u = profilemodel(profilepic=request.FILES['img'],pancard=request.FILES['pancard'],adhaarcard=request.FILES['adhaarcard'],anualincome=request.POST['annualincome'],bankdetails=request.POST['bankaccount'])
        u.save()
    else:

        u = uploadPrivate(profilepic=request.FILES['img'], pancard=request.FILES['pancard'],
                   adhaarcard=request.FILES['adhaarcard'], anualincome=request.POST['annualincome'],
                   bankdetails=request.POST['bankaccount'])
        u.save()



    return HttpResponse("you are file sucessfully uploaded")