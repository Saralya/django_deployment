from django.shortcuts import render
from login_app import forms
from django.contrib.auth.models import User
from login_app.models import UserInfo

# for login authentication, ei module gula import korte hobe
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def index(request):
    dict={}
    if request.user.is_authenticated:  # jodi user logged in obosthay thake,
        current_user = request.user  # tahole current_user variable e user er info gula niye nibo
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__pk=user_id)
        # jokhon 2ta model OneToOne/ManyToOne ei type er relation thakbe tokhon 2ta column name k separate korte hobe __ diye
        # user__pk er pk denote kore User model er pk (id) and...
        # user__pk er user denote kore, oi pk er basis e UserInfo model e j user ase tar data gula (fb_id & profile_pic)
        dict = {
        'user_basic_info':user_basic_info,
        'user_more_info': user_more_info,}
        # ei dict ta if condition er vitor likhte hobe..na hoy error dibe
    return render(request, 'login_app/index.html', context=dict)


def register(request):

    registered = False
    
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)  
        # form er input gula data er moddhe rakhlam jate pore ei data gula niye kaj kora jay...
        # and input soho pura form ta k user_form variable e save korlam
        user_info_form = forms.UserInfoForm(data=request.POST) 

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()  # user_form ta k user variable e save korlam
            user.set_password(user.password)  # set_password diye password encrypt kora hoy
            user.save() # User model e input gula save holo

            user_info = user_info_form.save(commit=False)
            user_info.user = user 
            # UserInfo model er user field e user variable (24 no. line) ta k store korlam...
            # Etar karone 2ta form & model (User & UserInfo) connected hobe 

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()  # UserInfo model e input gula save holo
            registered = True

    else:
        user_form = forms.UserForm()
        user_info_form = forms.UserInfoForm()
    dict = {
        'user_form': user_form,
        'user_info_form': user_info_form,
        'registered': registered,
    
    }
    return render(request, 'login_app/register.html', context=dict)



def login_page(request):
    return render(request, 'login_app/login.html', context={})

    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        # login.html er input tag er name field e ja likhsi seta ekhaner get() e likhbo
        
        user = authenticate(username=username, password=password)
        # authenticate function diye check kora hoy j User model er username r password er sathe..
        # input gula milse kina and result ta user variable e store kore (true/false)

        if user:  # jodi user e true save hoy,
            if user.is_active:  # and jodi user active thake
                login(request, user)  # tahole login function diye user k login korabo
                return HttpResponseRedirect(reverse('login_app:index'))
                # jodi return render diye login_app:index call kori tahole index view te niye geleo url pattern change hobe na..
                # url e user_login/ e dekhabe..tai HttpResponse(reverse()) use kora safe



            else:
                return HttpResponse("Account is not active!!")

        else:
            return HttpResponse("Login details are wrong!!")
    else:
        return HttpResponseRedirect(reverse('login_app:login'))


@login_required   # jodi user login obosthay thake taholei logout korte parbe
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:index'))
    # jodi logged in na thekeo keu logout e click kore tahole take login page e niye jete hobe..
    # seta korar jonno settings.py e LOGIN_URL = '/login/' likhe dite hobe


        
            

