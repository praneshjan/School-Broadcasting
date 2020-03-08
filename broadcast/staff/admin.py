from django.contrib import admin
from staff.models import User, Parent, Staff, Status, Message, Message_track, Grade, Student, UserProxy
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
        password = self.cleaned_data["password"]
        username = self.cleaned_data["username"]
        if username in password:
            raise forms.ValidationError('Entered password and username are similar')
        return self.cleaned_data
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
        
class UserProxyForm(forms.ModelForm):
    class Meta:
        model = UserProxy
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
    save_on_top = True
    change_list_template = "admin/change_list.html"
    list_display= ['username','password']


class ParentInline(admin.StackedInline):
    model = Parent
    extra = 0
    classes = ('grp-collapse grp-open',)

class ParentAdmin(admin.ModelAdmin):
    save_on_top = True
    form = UserForm
    inlines = [ParentInline]
    class Meta:
        model = User

class StaffInline(admin.StackedInline):
    model = Staff
    extra = 0
    classes = ('grp-collapse grp-open',)
class StaffAdmin(admin.ModelAdmin):
    save_on_top = True
    form = UserProxyForm
    inlines = [StaffInline]
    class Meta:
        model = UserProxy

class GradeAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list.html"
    autocomplete_lookup_fields = {
        'generic': [['content_type', 'id'], ['relation_type', 'grade_name']],
    }


admin.site.register(User, UserAdmin)
admin.site.register(Parent)
admin.site.register(Staff)
admin.site.register(Message)
admin.site.register(Message_track)
admin.site.unregister(Group)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Student)