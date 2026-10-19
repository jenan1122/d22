from operator import index

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

class person:
    def __init__(self,username,password):
        self.username = username
        self.password = password
people=[]

class personForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password",widget=forms.PasswordInput)

def index(request):
    return render(request,'d2/index.html',{"people": people})

def add(request):
    if request.method == "POST":
        form = personForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            p = person(username,password)
            people.append(p)
            return HttpResponseRedirect(reverse('d2:index'))
    else:
        form = personForm()

    return render(request,'d2/add.html',{"form":form})


# Create your views here.
