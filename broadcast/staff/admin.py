from django.contrib import admin
from staff.models import User, Parent, Staff, Status, Message, Message_track, Grade, Student
from django.contrib.auth.models import Group
# Register your models here.
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        emailid = self.cleaned_data.get('email')
        if not 'gmail.com' in emailid:
            raise forms.ValidationError('Entered Domain is wrong')
        return self.cleaned_data
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display= ['username','password']

admin.site.register(User,UserAdmin)
admin.site.register(Parent)
admin.site.register(Status)
admin.site.register(Staff)
admin.site.register(Message)
admin.site.register(Message_track)
admin.site.unregister(Group)
admin.site.register(Grade)
admin.site.register(Student)