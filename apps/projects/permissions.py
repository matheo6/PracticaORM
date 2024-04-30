from rest_framework.permissions import BasePermission
from .models import Project,Member


class IsMemberOrOwner(BasePermission):
    def has_permission(self, request, view):

        user= request.user
        project= Project.objects.filter(id=request.data.get("project"))       
        if project.exists():
            project= project.first()
            print(project.owner.id)
            return project.owner.id == user.id or Member.objects.filter(user= user,project=project).exists()
        else:
            return False    