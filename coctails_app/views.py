from django.shortcuts import render
from django.http import HttpResponse
from .forms.AddCoctailForm import AddCoctailForm

# Create your views here.

def index(request):
    form = AddCoctailForm()
    return render(request, 'coctails_app/index.html',{'form': form} )