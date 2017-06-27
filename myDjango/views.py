from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def login(request):
    c={}
    c.update(csrf(request))
    return render(request,)