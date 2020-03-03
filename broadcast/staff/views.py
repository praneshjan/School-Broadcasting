from django.shortcuts import render, redirect, HttpResponse
from staff.decorators import usercheck
from staff.forms import publishForm
# Create your views here.


def homepage(request):
    return render(request,'homepage.html')

@usercheck
def check_view(request):
    return redirect('')

def dashboard(request):

    return render(request,'staff/dashboard.html')

def publishView(request):
    if request.user.is_teacher:
        if request.method == 'POST':
            return HttpResponse(request.user.username)
        else:
            pv = publishForm()
        return render(request,'staff/publish.html',{'form': pv})