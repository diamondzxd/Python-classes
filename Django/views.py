views.py references

#Default Packages

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def Page1(request):
	return HttpResponse("Hello World")


def Page2(request):
	output='''
			<html>
				<head>
				</head>
				<body>
				<h1>Hello Workd</h1>
				</body>
				</html>
			'''
	return HttpResponse(output)