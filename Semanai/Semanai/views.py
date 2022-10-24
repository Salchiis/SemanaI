from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')