from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *

# Create your views here.
from datetime import datetime

class ProjectAPIView(APIView):
    def get(self, request):
        projects= Project.objects.all()


        data= [
            {
                "id": project.id,
                "name": project.name
            }
            for project in projects
        ]

        return Response(data)
    
    def post(self,request):

        print(request.data)
        project= Project()
        project.name= request.data.get('name',"")
        project.init_date= datetime.now()
        end_date= request.data.get('end_date',"")
        project.end_date= datetime.strptime(end_date, '%d-%m-%Y %H:%M:%S')
        project.save()
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
        