from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
def usercheck(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_teacher:
            return redirect('/staff/dashboard')
        elif request.user.is_parent:
            return redirect('/parent/dashboard')
            #return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap