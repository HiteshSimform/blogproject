from django.core.exceptions import PermissionDenied

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request,*args,**kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied
            if request.user.role != role:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

admin_required = role_required('admin')
author_required = role_required('author')
reader_required = role_required('reader')