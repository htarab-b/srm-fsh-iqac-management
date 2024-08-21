from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import *

# Authenticate
class LoginView(FormView):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin')
        return render(request, 'login.html', {'message': 'Invalid credentials! Try again'})

# Views
class FormFillView(FormView):
    def get(self, request):
        if request.GET.get('form') == 'Student':
            return render(request, 'studentform.html')
        elif request.GET.get('form') == 'Staff':
            return render(request, 'staffform.html')
        else:
            return render(request, 'formchoice.html')
    def post(self, request):
        Name = request.POST.get('Name')
        ID = request.POST.get('ID')
        Department = request.POST.get('Department')
        Phone = request.POST.get('Phone')
        Email = request.POST.get('Email')
        Subject = request.POST.get('Subject')
        Purpose = request.POST.get('Purpose')
        Type = request.POST.get('Type')
        FormDetailsModel.objects.create(
            Name = Name,
            RegID = ID,
            Department = Department,
            Phone = Phone,
            Email = Email,
            Subject = Subject,
            Purpose = Purpose,
            Type = Type
        )
        details = FormDetailsModel.objects.get(
            Name = Name,
            RegID = ID,
            Department = Department,
            Phone = Phone,
            Email = Email,
            Subject = Subject,
            Purpose = Purpose,
            Type = Type
        )
        return render(request, 'report.html', {'details': details})
        
class AdminView(LoginRequiredMixin, ListView):
    login_url = 'login'
    def get(self, request):
        if request.GET.get('FormID'):
            details = FormDetailsModel.objects.filter(
                id = request.GET.get('FormID'),
            )
            if details.exists(): details = details.first()
            else: messages.success(request, 'Invalid Form ID')
            return render(request, 'adminreport.html', {'details': details})
        else:
            return render(request, 'admin.html')
    def post(self, request):
        user = request.user.username
        formDetails = FormDetailsModel.objects.get(
            id = request.GET.get('FormID'),
        )
        if user == 'coordinator':
            formDetails.Coordinator_Approval = 'YES'
        elif user == 'dean':
            formDetails.Dean_Approval = 'YES'
        elif user == 'deputydean':
            formDetails.DeputyDean_Approval = 'YES'
        elif user == 'provc':
            formDetails.ProVC_Approval = 'YES'
        formDetails.save()
        messages.success(request, 'Form Approved by '+user)
        return render(request, 'adminreport.html', {'details': formDetails})