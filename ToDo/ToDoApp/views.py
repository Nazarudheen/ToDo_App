from django.shortcuts import render,redirect
from django.contrib import messages
from ToDoApp.models import SignUpDB,Projects,TaskDB

# Create your views here.
def SignUpPage(request):
    return render(request,"SignUp.html")

def HomePage(request):
    data = Projects.objects.all()
    return render(request,"Home.html",{'data':data})

def EditPage(request,uid):
    x = TaskDB.objects.get(id=uid)
    return render(request,"EditPage.html",{'x':x})

def SignupPage(request):
    if request.method == "POST":
        n = request.POST.get('SName')
        e = request.POST.get('SEmail')
        p = request.POST.get('SPassword')

        obj = SignUpDB(Name=n, Email=e, Password=p)
        obj.save()
        messages.success(request,"Registered")
        return redirect(SignUpPage)

def LoginUser(request):
    if request.method=="POST":
        un = request.POST.get('name')
        pd = request.POST.get('password')
        if SignUpDB.objects.filter(Name=un,Password=pd).exists():
            request.session['Name']=un
            request.session['Password']=pd
            messages.success(request, "Login Successfull")
            return redirect(HomePage)
        else:
            messages.warning(request, "Username does't exist")
            return redirect(SignUpPage)
    messages.error(request, "Incorrect password")
    return redirect(SignUpPage)

def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    messages.success(request, "Logout Successfully")
    return  redirect(SignUpPage)

def psave(request):
    if request.method=="POST":
        p = request.POST.get("Ptitle")
        obj = Projects(Title=p)
        obj.save()
        return redirect(HomePage)
def delProject(request,pid):
    x = Projects.objects.filter(id=pid)
    x.delete()
    return redirect(HomePage)

def deltask(request,tid):
    x = TaskDB.objects.filter(id=tid)
    x.delete()
    return redirect(HomePage)

def Task_Page(request,T):
    y = Projects.objects.get(Title=T)
    x = TaskDB.objects.filter(TitleT=T)
    return render(request,"TaskPage.html",{'x':x,'y':y})

def Tsave(request):

    if request.method=="POST":
        e = request.POST.get("title")
        p = request.POST.get("TTask")
        c = request.POST.get("TUdate")
        u = request.POST.get("TDiscription")
        s = request.POST.get('Tstatus', False)
        obj = TaskDB(Task=p,Discription=u,status=s,Udate=c,TitleT=e)
        obj.save()
    return redirect(HomePage)

def upadtetask(request,uid):
    if request.method == "POST":
        e = request.POST.get("title")
        p = request.POST.get("TTask")
        c = request.POST.get("TUdate")
        u = request.POST.get("TDiscription")
        s = request.POST.get('Tstatus', False)
        TaskDB.objects.filter(id=uid).update(Task=p, Discription=u, status=s, Udate=c, TitleT=e)

    return redirect(HomePage)


