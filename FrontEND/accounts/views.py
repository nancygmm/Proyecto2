from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoListItem 
from django.http import HttpResponseRedirect 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic



def store(request):
    return render(request, 'medical/store.html')

def donar(request):
    return render(request, 'medical/resultado.html')

def resultado(request):
    if request.method == 'POST':
        # Procesar los datos del formulario y realizar acciones necesarias
        # ...
        return render(request, 'medical/resultado.html')
    else:
        # Código para manejar una solicitud GET (opcional)
        # ...
        return render(request, 'medical/store.html')
    
def my_view(request):
    my_string = "../../static/accounts/scarymovie.jpg"
    return render(request, 'resultado.html', {'my_string': my_string})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


