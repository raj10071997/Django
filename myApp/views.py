# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .MySerializer import Serializer
from django.shortcuts import render
from myApp.models import AppDhanraj
from django.template.loader import get_template
from django.http import HttpResponse
from myApp.forms import LoginForm
from django.views.generic import TemplateView
# Create your views here.

def login(request):
	username = "not logged in"

	if request.method == "POST":
		MyLoginForm = LoginForm(request.POST)

		if MyLoginForm.is_valid():
			username = MyLoginForm.cleaned_data['username']
	else:
		MyLoginForm = LoginForm()

	return render(request, 'loggedin.html', {"username " : username})



class AboutView(TemplateView):
	template_name = "Login.html"

class MyList(APIView):

	def get(self, request):
		dhanraj = AppDhanraj.objects.all()
		serializer = Serializer(dhanraj, many = True)
		return Response(serializer.data)

	def post(self):
		pass


def hello(request,iddhanraj=1):
	return render(request,'helloo.html', {'articles': AppDhanraj.objects.get(id=iddhanraj) })

