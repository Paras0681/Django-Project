from django.contrib.auth import authenticate
from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User, auth
from . models import Report_info
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username Taken")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email-id Taken")
            return redirect('register')
        elif User.objects.filter(password=password).exists():
            messages.info(request, "Password Taken")
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save();
            messages.info(request, 'New User created')
        return redirect('index')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def report(request):
    if request.method == 'POST':
        try:
            user = request.user
            select_location = request.POST.get('select_location')
            incident_dept = request.POST.get('incident_dept')
            date = request.POST.get('date')
            incident_location = request.POST.get('incident_location')
            severity = request.POST.get('severity')
            sus_cause = request.POST.get('sus_cause')
            imm_action = request.POST.get('imm_action')
            incident_types = request.POST.get('incident_types')
            if not user or not select_location or not incident_dept:
                messages.error(request, 'All fields are mandatory')
                return redirect('report')
            data = Report_info(location=select_location, incident_department=incident_dept, date=date, incident_location=incident_location, initial_severity=severity, suspected_cause=sus_cause,incident_types=incident_types, action_taken=imm_action, user=user)
            data.save()
            messages.info(request, 'New Report created')
            return render(request, 'report.html')
        except Exception as e:
            messages.error(request,'An error occured.')
            return redirect('report')

    return render(request, 'report.html')


class HomeView(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)


class Saved_View(View):
    template_name = 'saved_incidents.html'
    def get(self, request):
        data = Report_info.objects.all()
        return render(request, self.template_name, {'data':data})


class Sent_View(View):
    template_name = 'saved_incidents.html'
    def get(self, request):
        data = Report_info.objects.filter(user=request.user)
        return render(request, self.template_name, {'data':data})