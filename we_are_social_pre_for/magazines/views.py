# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Magazine
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def all_magazines(request):
    magazine = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": magazine})

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')