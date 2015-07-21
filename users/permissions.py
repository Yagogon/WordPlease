from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la accion (GET, POST, PUT o DELETE)
        :param request:
        :param view:
        :return:
        """
        # si quiere crear un usuario, sea quien sea puede
        if view.action == 'create':
            return True

        # si no es POST, el superusuario siempre puede
        elif request.user.is_superuser:
            return True

        # si es un GET a la vista de detalle, tomo la decision en has_object
        elif view.action in ['retrieve', 'update', 'destroy']:
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
        return request.user.is_superuser or request.user == obj
