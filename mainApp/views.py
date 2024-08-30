from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseForbidden
from django.db.models import Q
from random import randrange
from django.conf import settings
from django.core.mail import send_mail

def home(Request):
    if(Request.method=="POST"):
        p = Request.POST.get("password")
        cp = Request.POST.get("cpassword")
        print(p)
        if(p==cp):
            b = Users()
            b.username = Request.POST.get("uname")
            b.email = Request.POST.get("email")
            b.password = p
            print(b.username)
            user = User(username=b.username,email=b.email)
            if(user):
                user.set_password(p)
                user.save()
                b.save()
                # subject = 'Your Account is Created: Team Vshop'
                # message =  "Hello "+b.name+"\nThanks to Create a Buyer Account with Us\nNow You can buy Our Latest Products\nTeam Vshop"           
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = [b.email, ]
                # send_mail( subject, message, email_from, recipient_list )
                return redirect("/")
                # return redirect("/registration-thanks")
            else:
                messages.error(Request,"Password and Confirm Password doesn't matched!!!")
        else:
            messages.error(Request,"Password and Confirm Password doesn't matched!!!")
    return render(Request,"my-account.html")


def loginLogic(Request):
    if(Request.method=="POST"):
        username = Request.POST.get("uname")
        password = Request.POST.get("password")
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(Request,user)
            if(user.is_superuser):
                return redirect("/admin-dashboard")
            else:
                return redirect("/user-dashboard")
        else:
            messages.error(Request,"Invalid Username or Password!!!")
    return render(Request, "my-account.html")

def logoutLogic(Request):
    logout(Request)
    return redirect("/login")

def resume_Page(Request,id,name):
    data = Resume.objects.get(id=id)
    return render(Request,"resume/index.html",{"data":data})

#User Dashboard
@login_required(login_url='/login/')
def user_dashboard(Request):
    username=Request.user.username
    data=Resume.objects.filter(username=username).order_by('id').reverse()
    
    paginator = Paginator(data, 100)  # Show 10 posts per page
    page_number = Request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    current_page = page_posts.number
    total_pages = paginator.num_pages
    page_range = range(max(current_page - 2, 1), min(current_page + 3, total_pages + 1))
    return render(Request,'user/index.html',{'page_posts':page_posts,'page_range': page_range})


@login_required(login_url="/login/")
def user_add_resume(Request):
    
    msg=''
    username=Request.user.username
    if (Request.method == "POST"):
        r=Resume()
        r.username=username
        r.name=Request.POST.get("name")
        r.phone=Request.POST.get("phone")
        r.email=Request.POST.get("email")
        r.address=Request.POST.get("address")
        r.image=Request.FILES.get("image")
        r.education=Request.POST.get("education")
        r.skills=Request.POST.get("skills")
        r.internship=Request.POST.get("internship")
        r.experience=Request.POST.get("experience")
        r.project=Request.POST.get("project")
        r.video=Request.FILES.get("video")        

        r.save()
        msg="Done"
        return redirect(f"/resume/{r.name}-{r.id}/")
    return render(Request,'user/add-resume.html',{'msg':msg,})


@login_required(login_url="/login/")
def user_update_resume(Request,id):
    data=Resume.objects.get(id=id)
    msg=''
    
    if (Request.method == "POST"):
        data.name=Request.POST.get("name")
        data.phone=Request.POST.get("phone")
        data.email=Request.POST.get("email")
        data.address=Request.POST.get("address")
        if(Request.FILES.get("image")):
            data.image=Request.FILES.get("image")
        data.education=Request.POST.get("education")
        data.skills=Request.POST.get("skills")
        data.internship=Request.POST.get("internship")
        data.experience=Request.POST.get("experience")
        data.project=Request.POST.get("project")
        if(Request.FILES.get("video")):
            data.video=Request.FILES.get("video")        

        data.save()
        msg="Done"
        return redirect("/user-dashboard")
    return render(Request,'user/update-resume.html',{'msg':msg,"data":data})

def user_delete_resume(Request,id):
    p=Resume.objects.get(id=id)
    p.delete()
    return redirect('/user-dashboard')

