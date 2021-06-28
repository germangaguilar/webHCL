from django.shortcuts import render,redirect
from . import models
from django.http import Http404
from django.http import HttpResponse
import pdb
from django.core.mail import send_mail
# Create your views here.

from django.contrib.auth import authenticate, login, logout, get_user_model


# Create your views here.
from .forms import LoginForm, RegisterForm, Pickdates



def travelclick(request):
     return redirect("https://reservations.travelclick.com/114062#/datesofstay")

def pickdates(request):
    dateform=Pickdates(request.GET or None)
    if dateform.isvalid():
        inicio=dateform.cleaned_data.get('Fecha de entrada')
        salida=dateform.cleaned_data.get('Fecha de salida')
        adultos=dateform.cleaned_data.get('Adultos')
        ninos=dateform.cleaned_data.get('Niños')

    #return render(request, "registration.html", {"dateform": dateform})
    return render(request, "disponibilidad.html", inicio=inicio, salida=salida, adultos=adultos, ninos=ninos)

User = get_user_model()

def register_view(request, backend='django.contrib.auth.backends.ModelBackend'):
    form1 = LoginForm(request.POST or None)
    if form1.is_valid():
        email = form1.cleaned_data.get("email")
        password = form1.cleaned_data.get("password")
        try:
            user = authenticate(request, username=email, password=password, backend= 'django.contrib.auth.backends.ModelBackend') #hosting
        except:
            user = authenticate(request, username=email, password=password) #local

        if user != None:
            # user is valid and active -> is_active
            # request.user == user

            try:
                login(request, user, backend= 'django.contrib.auth.backends.ModelBackend') #hosting
            except:
                login(request, user) #local
            return redirect("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            return redirect("/invalid-password")
            request.session['invalid_user'] = 1 # 1 == True

    form2 = RegisterForm(request.POST or None)
    if form2.is_valid():
        email = form2.cleaned_data.get("email")
        nombre = form2.cleaned_data.get("nombre")
        apellidos =form2.cleaned_data.get("apellidos")
        password = form2.cleaned_data.get("password1")
        password2 = form2.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username=email,
                email=email,
                password=password,
                first_name=nombre,
                last_name=apellidos)
        except:
            user = None
        if user != None:
            try:
                login(request, user, backend= 'django.contrib.auth.backends.ModelBackend') #hosting
            except:
                login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1 # 1 == True
    return render(request, "registration.html", {"form2": form2,"form1": form1 })

#mi idea es mezclaro con el anterior
#usar form1 y form2? revisa el html
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user != None:
            # user is valid and active -> is_active
            # request.user == user
            login(request, user)
            return redirect("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1 # 1 == True
    return render(request, "forms.html", {"form": form})

def logout_view(request):
    logout(request)
    # request.user == Anon User
    return redirect("/register")


def index(request):
    ro=models.rooms.objects.all()
    return render(request,"index.html",{"ro":ro})

def base(request):
    ro=models.rooms.objects.all()
    return render(request,"base.html",{"ro":ro})

def rooms(request):
    ro=models.rooms.objects.all()
    return render(request,"rooms2.html",{"ro":ro})

def inicio(request):
    ro=models.rooms.objects.all()
    return render(request,"inicio.html",{"ro":ro})

def contact(request):
    ro=models.rooms.objects.all()
    return render(request,"about2.html",{"ro":ro})

def servicios(request):
    ro=models.rooms.objects.all()
    return render(request,"spaces.html",{"ro":ro})

def about(request):
    ro=models.rooms.objects.all()
    return render(request,"about.html",{"ro":ro})

def base(request):
    ro=models.rooms.objects.all()
    return render(request,"base.html",{"ro":ro})

def search(request):
    ro=models.rooms.objects.all()
    val1=request.POST['num1']

    return render(request,"search.html",{"ro":ro,"val1":val1})


def book(request):

    return render (request,"booking.html")

def ofertas(request):
    ro=models.rooms.objects.all()
    return render (request,"ofertas.html",{"ro":ro})




def confirm(request):

     val8=int(request.POST['adult'])
     val10=int(request.POST['child'])
     val11=int(request.POST['nights'])

     cost=(val11*((val8*1000)+(val10*500)))
     request.session['val12']=request.POST['name']
     request.session['val2']=request.POST['adult']
     request.session['val3']=request.POST['child']
     request.session['val13']=request.POST['no']
     request.session['val9']=request.POST['room_code']
     request.session['val6']=request.POST['nights']
     request.session['val30']=request.POST['checkin']
     request.session['var']=cost
     request.session['val150']=request.POST['email']
     return render(request,"confirm.html",{'cost':cost})






def payment(request):
    if 'val700' not in request.session:
        return redirect('/')
    cost=request.session['val700']
    return render(request,"Payment.html",{'cost':cost})


def success(request):


    guest1=models.guest()
    guest1.Head_name=request.session['val12']
    guest1.No_of_adults=request.session['val2']
    guest1.no_of_children=request.session['val3']
    guest1.Identity_no=request.session['val13']
    guest1.Room_code=request.session['val700']
    guest1.No_of_nights=request.session['val6']


    guest1.save()

    ro=models.rooms.objects.all()
    for ro in ro :
            if (ro.Roomcode==request.session['val700']):
                    ro.Availible=False
                    ro.save()
                    break
    val180=request.session['val150']
    # send_mail('Payment Received','Room Booked','workjash@hushmail.com',['{}'.format(val180)],fail_silently=True)
    return render (request,"success.html")

def cancel(request):
    del request.session['val700']
    return redirect('/')
