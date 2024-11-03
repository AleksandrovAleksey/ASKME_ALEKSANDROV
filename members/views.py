from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def members(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())

def ask(request):
  template = loader.get_template('ask.html')
  return HttpResponse(template.render())

def question(request):
  template = loader.get_template('question.html')
  return HttpResponse(template.render())

def bender(request):
  template = loader.get_template('bender.html')
  return HttpResponse(template.render())

def settings(request):
  template = loader.get_template('settings.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def signup(request):
  template = loader.get_template('sign up.html')
  return HttpResponse(template.render())