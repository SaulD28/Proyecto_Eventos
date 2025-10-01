from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Evento


def home(request):
    return render(request, 'home.html')

def table(request):
    return render(request, 'table.html')

def get_eventos(request):
    eventos = Evento.objects.all().values()
    return JsonResponse(list(eventos), safe=False)