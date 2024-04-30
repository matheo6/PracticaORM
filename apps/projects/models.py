from django.db import models

# import from other apps
from apps.users.models import User
# Create your models here.
class Project(models.Model):
    owner= models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=60,null=False,blank=False)
    init_date= models.DateTimeField(auto_now_add=True)
    end_date= models.DateTimeField()
    
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    prioritys={
        "HG":"Hight",
        "Md":"Medium",
        "Lw":"Low"        
    }
    description= models.CharField(max_length=250)
    priority= models.CharField(max_length=120,choices=prioritys,default="LW")
    end_date= models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    is_complete = models.BooleanField(default=False)
    #ownerstasks= models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.description

class Comment(models.Model):
    
    init_date= models.DateTimeField()
    content= models.CharField(max_length=120)
    task= models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    users=models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Member(models.Model):

    rols={
        "DEV":"Developer",
        "PO":"ProductOwner",
        "TL":"TeamLider",
        "SM":"ScrumMaster",
        "DBA":"DataBaseAdministrator",
        
    }
    rol= models.CharField(max_length=60,choices=rols,default="DEV")
    date_joined= models.DateTimeField(null=True)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    


class OwnersTask(models.Model):
    task= models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)