from rest_framework.permissions import BasePermission

class IsMemberOrOwner(BasePermission):
    def has_permission(self, request, view):
        user= request.user

        print("pasando por el permiso")
        return True