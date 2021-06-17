
from django.shortcuts import render
from .forms import NewForm,DataCollectionForm,UserProfileInfoForm,UserForm
from .models import users
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

@login_required
def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse(index))
    return HttpResponseRedirect('help')

@login_required
def special(request):
    return HttpResponse(request,"You are logged Nice")


def help(request):
    date = datetime.date.today()
    time = datetime.datetime.now()
    dict_t = {"num" : "hello this is my world", "date": date, 'time': time}
    return render(request,'AppTwo/help.html',dict_t)

def formView(request):
   
    frm = NewForm()
    if request.method == 'POST':
        frm = NewForm(request.POST)
        if frm.is_valid():
            print("valid Data")
            print(frm.cleaned_data['fname'])
            print(frm.cleaned_data['lname'])
            print(frm.cleaned_data['email'])
            return index(request)
    return render (request, 'AppTwo/form.html',{'form':frm})
    

def userlist(request):
    usr_l = users.objects.order_by('fname')
    mod = {"mod":usr_l}
    return render (request, 'AppTwo/userlist.html',mod)


def datacoll(request):
    frms= DataCollectionForm()
    if request.method == 'POST':
        frms = DataCollectionForm(request.POST)
        if frms.is_valid():
            print("valid Data")
            frms.save(commit=True)
            return index(request)
    return render (request, 'AppTwo/datacoll.html',{'form':frms})





def register(request):
    registered = False 
    if request.method == 'POST':
        user_form = UserForm(data= request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile =profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            registered = True
        else:
            print("user_form,profile_form.errors")
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'AppTwo/reg.html',
                             {'user_form':user_form,
                             'profile_form':profile_form,
                             'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                # return HttpResponseRedirect(reverse('index'))
                return index(request)
            else:
                return HttpResponse("Acoount Not active")
        else:
            print("someone is tried to loged in")
            print('username:{} and password:{}'.format(username,password))
            return HttpResponse("invalid login details ")
    else:
        return render(request,'AppTwo/login_page.html',{})



        
    