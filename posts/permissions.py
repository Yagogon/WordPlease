from rest_framework.permissions import BasePermission
from django.utils.timezone import now

class PostPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la accion (GET, POST, PUT o DELETE)
        :param request:
        :param view:
        :return:
        """
        if view.action == 'create' and request.user.is_authenticated:
            return True

        elif request.user.is_superuser:
            return True

        elif view.action in ['retrieve', 'update', 'destroy', 'list']:
            return True

        else:
            return False


    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la accion (GET, POST, PUT o DELETE)
        sobre el object obj
        :param request:
        :param view:
        :param obj:
        :return:
        """
        # si es un superadmin, o el usuario autenticado intenta
        # hacer GET, PUT o DELETE sobre su mismo perfil
        return request.user.is_superuser or request.user == obj.owner or obj.publish_date < now
