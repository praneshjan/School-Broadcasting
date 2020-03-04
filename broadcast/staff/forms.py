from django import forms
from django.forms import ModelForm
from staff.models import Message

class PublishForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget= forms.Textarea)
    file_upload = forms.FileField()

class PublishmodelForm(ModelForm):
    class Meta:
        model = Message
        fields = ['topic_title','topic_body','file_path']