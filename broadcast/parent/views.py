from django.shortcuts import render, HttpResponse
from staff.models import Message_track, Parent, Status, Message
# Create your views here.


def parent_dashboard(request):
    return render(request,'parent/dashboard.html')

def parentUseen(request):
    user = request.user
    parent = Parent.objects.get(parent_id=user)
    status = Status.objects.get(status_name='unseen')
    mt = Message_track.objects.filter(parent_id=parent, status=status)
    return render(request,'parent/unseen.html',{'message' : mt})

def messageView(request,id):
    message = Message.objects.get(id = id)
    newstatus = Status.objects.get(status_name = 'seen')
    user = request.user
    parent = Parent.objects.get(parent_id=user)
    status = Status.objects.get(status_name='unseen')
    mt = Message_track.objects.get(parent_id=parent, status=status, message_id=message)
    mt.status = newstatus
    mt.save()  
    return render(request,'parent/messageview.html',{'msg':message})


def filedownload(request,id):
    message = Message.objects.get(id = id)
    message = message.file_path
    filename = message.name
    filename = filename.split('/')[-1]
    body = message.read()
    response = HttpResponse(body,'application/force-download')
    response['Content-Disposition'] = 'inline; filename='+filename
    return response

def pdfview(request,id):
    message = Message.objects.get(id = id)
    message = message.file_path
    filename = message.name
    filename = filename.split('/')[-1]
    body = message.read()
    response = HttpResponse(body,'application/pdf')
    response['Content-Disposition'] = 'inline; filename='+filename
    return response

def parentSeen(request):
    user = request.user
    parent = Parent.objects.get(parent_id=user)
    status = Status.objects.get(status_name='seen')
    mt = Message_track.objects.filter(parent_id=parent, status=status)
    return render(request,'parent/seen.html',{'message' : mt})

def oldmessageView(request, id):
    message = Message.objects.get(id = id)
    return render(request,'parent/messageview.html',{'msg':message})