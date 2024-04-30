from rest_framework import serializers
from .models import Project,Task,Comment

class ProjectSerializerModel(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= "__all__"

class TaskSerializerModel(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields= "__all__"



class CommentSerializerModel(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields= "__all__"
    def validate_content(self,value):
        malasPalabras=["bobo","tonto","estupido"]
        for x in malasPalabras:
            if x in value:
                print(x," es una mala malasPalabras")
                raise serializers.ValidationError(" Mala palabra detectada, porfavor usar un lenguaje apropiado")
            else:
                print("No es una mala palabra")
        return value
            
class ProjectSerializer(serializers.Serializer):
    name= serializers.CharField(max_length=60)
    init_date= serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField()


    def validate(self, attrs):
        #if attrs.get("end_date")< datetime.now():
        #    raise serializers.ValidationError("The end date must be older than actually date")
        return super().validate(attrs)

    def create(self, validated_data):
        Project(**validated_data).save()
        
        return self.data

class TaskDetailSerializerModel(serializers.ModelSerializer):

    project = ProjectSerializer()

    class Meta:
        model= Task
        fields= [
            "id",
            "description",
            "end_date",
            "is_complete",
            "project",
        ]