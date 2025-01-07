from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

class UserIsAdminOrModerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user.role != 'admin' and self.request.user.role != 'moderator':
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

class UserIsOwnerAndAdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != self.request.user and request.user.role != "admin" and request.user.role != "moderator":
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


