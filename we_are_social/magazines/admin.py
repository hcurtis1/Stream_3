# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Magazine
from .models import Purchase

from django.contrib import admin

# Register your models here.

admin.site.register(Magazine)
admin.site.register(Purchase)