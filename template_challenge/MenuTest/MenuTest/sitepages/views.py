# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def home(request):
    now = datetime.datetime.now()
    return render(request, "MenuTest/home.html", {"current_date": now})


def about(request):
    return render(request, "MenuTest/about.html")


def contact(request):
    return render(request, "MenuTest/contact.html", {"first_name": "Henry", "last_name": "Curtis",
                                                     "telephone_no": "07473251738"})
