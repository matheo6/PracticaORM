from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import ProjectSerializer,ProjectSerializerModel,TaskSerializerModel,CommentSerializerModel
# Create your views here.
from datetime import datetime
from rest_framework.viewsets import ModelViewSet

class ProjectViewSet(ModelViewSet):
    queryset= Project.objects.all()
    serializer_class= ProjectSerializerModel

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class= TaskSerializerModel

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class= CommentSerializerModel

    
class ProjectAPIView(APIView):
    def get(self, request):
        projects= Project.objects.all()
        serializer= ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self,request):

        print(request.data)
        project= Project()
        serializer= ProjectSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})
    
    def delete(self,request):
        id = request.data.get("id")
        project= Project.objects.get(id=id)
        project.delete()
        return Response({})
    
    def patch(self,request):
        id = request.data.get("id")
        project= Project.objects.get(id=id)
        project.name= request.data.get("name",project.name)
        project.save()
        return Response({
            "id":project.id,
            "name":project.name
        })
        

class TASKAPIREView(APIView):
    def get(self, request):
        tasks= Task.objects.all()
        data= [
            {
                "id":task.id,
                "description": task.description,
                "priority": task.priority,
                "project": task.project.name
            }
            for task in tasks
        ]
        return Response(data)
    
    def post(self,request):

        print(request.data)
        task= Task()
        task.description= request.data.get('description',"")
        task.priority= request.data.get('priority',"Md")
        id = request.data.get("project_id")
        task.project= Project.objects.get(id=id)
        end_date= request.data.get('end_date',"")
        task.end_date= datetime.strptime(end_date, '%d-%m-%Y %H:%M:%S')
        task.save()
        print(task.project.name)

        return Response({})
    
    def delete(self,request):
        id = request.data.get("id")
        task= Task.objects.get(id=id)
        task.delete()
        return Response({})
    
    def patch(self,request):
        id = request.data.get("id")
        task= Task.objects.get(id=id)
        task.description= request.data.get("description",task.description)
        task.save()
        return Response({
            "id":task.id,
            "description":task.description
        })
        