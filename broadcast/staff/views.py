from django.shortcuts import render, redirect, HttpResponse
from staff.decorators import usercheck
from staff.forms import PublishForm, PublishmodelForm
from staff.models import Grade, Staff, Message, Message_track, Student, Parent, Status
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
            user = request.user
            staff = Staff.objects.get(staff_id=user)
            grade = staff.grade_id
            pv = PublishForm(request.POST,request.FILES)
            print(request.FILES)
            if pv.is_valid():
                title = pv.cleaned_data['title']
                body = pv.cleaned_data['body']
                new_publish = Message(
                    grade_id = grade,
                    staff_id = staff,
                    file_path = request.FILES['file_upload'],
                    topic_body = body,
                    topic_title = title)
                new_publish.save()
                students = Student.objects.filter(grade_id = grade)
                for student in students:
                    parent = Parent.objects.get(student_id=student)
                    statusName = Status.objects.get(status_name = 'unseen')
                    mt = Message_track(
                        grade_id = grade,
                        message_id = new_publish,
                        parent_id = parent,
                        status = statusName,
                        )
                    mt.save()
                return redirect('/staff/dashboard')
        else:
            pv = PublishForm()
        return render(request,'staff/publish.html',{'form': pv})