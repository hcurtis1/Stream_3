# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Quotes_app.models import Quote
# Create your views here.

def get_quotes(request):
    return render(request, "Quotes/home.html", {'quotes_list': Quote.objects.all()})
