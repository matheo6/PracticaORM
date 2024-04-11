from django.contrib import admin
from .models import *


# Register your models here.
class ProjectsAmdin(admin.ModelAdmin):
    list_display = ["name","init_date","end_date"]

class ProjectsTask(admin.ModelAdmin):
    list_display= ["id", "project","description","end_date"]


class CommendAdmin(admin.ModelAdmin):
    list_display= ["id", "task","content","init_date"]

class Members(admin.ModelAdmin):
    list_display= ["rol", "date","user","project"]
class Owners(admin.ModelAdmin):
    list_display=["user","task"]

admin.site.register(Project,ProjectsAmdin)
admin.site.register(Task, ProjectsTask)
admin.site.register(Comment, CommendAdmin)
admin.site.register(Member, Members)
admin.site.register(Owner,Owners)