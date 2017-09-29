# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Magazine
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def all_magazines(request):
    magazine = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": magazine})

@csrf_exempt
def login_required(request):
    return render(request, "login.html")