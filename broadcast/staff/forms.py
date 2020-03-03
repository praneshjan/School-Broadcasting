from django import forms

class publishForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget= forms.Textarea)
    file_upload = forms.FileField()