from django.http import Http404
from django.shortcuts import redirect



def user_is_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        request_func = view_func(request, *args, **kwargs)
        return request_func
    return wrapper


def has_object_permission(obj_id,object_klass):
    def decorator(func):
        def wrapper(request,*args,**kwargs):
            try:
                obj = object_klass.objects.get(uuid=kwargs[obj_id])
                if not request.user == obj.user:
                    raise Http404('Not Possible!')
            except object_klass.DoesNotExist:
                Http404('Object DOES NOT EXIST')
            request_func = func(request,*args,**kwargs)
            return request_func
        return wrapper
    return decorator

