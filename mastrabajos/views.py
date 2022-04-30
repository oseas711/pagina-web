from django.shortcuts import render, redirect
from .forms import comentariosForm, userForm, loginForm
from .models import Empleos,Empresas
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView


# Create your views here.

def inicio(request):
    empleos = Empleos.objects.all()
    datos = {
        "empleos" : empleos,
        "forms"   : comentariosForm
    }
    if request.method == "POST":
        formulario = comentariosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["forms"]= formulario
            
    return render(request,'inicio.html', datos)

def buscar(request):
    if request.GET['busqueda']:
        query = request.GET['busqueda']
        empresas = Empresas.objects.filter(Marca=query)
        datos = {
        "empresas": empresas,
        
        }
        return render(request, 'buscar.html',datos)
    else:
        return render(request, 'buscar.html')


def about_us(request):
    empresas = Empresas.objects.all()
    datos = {
        "empresas" : empresas
    }
    return render(request,'about_us.html', datos)

def typography(request):
    return render(request,'typography.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

class Register(View):
    form_class = userForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs): 
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})
    def dispatch(self, request, *args, **kwargs):
                if request.user.is_authenticated:
                    return redirect(to='/')
                return super(Register, self).dispatch(request, *args, **kwargs)
            


class CustomLoginView(LoginView):
    form_class = loginForm
    def form_valid(self, form):
        form2Example3= form.cleaned_data.get('form2Example3')
        if not form2Example3:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(CustomLoginView, self).form_valid(form)