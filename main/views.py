from django.shortcuts import render,redirect
from . import models
from django.http import Http404
from django.http import HttpResponse
import pdb
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

from django.contrib.auth import authenticate, login, logout, get_user_model


# Create your views here.
from .forms import LoginForm, RegisterForm, ContactForm




def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry"
			body = {
			'first_name': form.cleaned_data['first_name'],
			'last_name': form.cleaned_data['last_name'],
			'email': form.cleaned_data['email_address'],
			'message':form.cleaned_data['message'],
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:inicio")

	form = ContactForm()
	return render(request, "inicio.html", {'form':form})

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
    return render(request,"eng-inicio.html",{"ro":ro})

def discover(request):
    ro=models.rooms.objects.all()
    return render(request,"eng-spaces.html",{"ro":ro})

def engrooms(request):
    ro=models.rooms.objects.all()
    return render(request,"eng-rooms.html",{"ro":ro})

def offers(request):
    ro=models.rooms.objects.all()
    return render(request,"eng-ofertas.html",{"ro":ro})

def frindex(request):
    return render(request,"fr-inicio.html")

def frrooms(request):
    return render(request,"fr-rooms.html")

def frdiscover(request):
    return render(request,"fr-spaces.html")

def froffers(request):
    return render(request,"fr-ofertas.html")



def base(request):
    ro=models.rooms.objects.all()
    return render(request,"base.html",{"ro":ro})

def rooms(request):
    ro=models.rooms.objects.all()
    return render(request,"rooms2.html",{"ro":ro})

def inicio(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry"
			body = {
			'first_name': form.cleaned_data['first_name'],
			'last_name': form.cleaned_data['last_name'],
			'email': form.cleaned_data['email_address'],
			'message':form.cleaned_data['message'],
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'germangarciaaguilar@gmail.com', ['germangarciaaguilar@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:inicio")

	form = ContactForm()
	return render(request, "inicio.html", {'form':form})

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






def ofertas(request):
    return render (request,"ofertas.html")
