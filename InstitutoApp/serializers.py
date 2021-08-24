from rest_framework import serializers
from InstitutoApp.models import Docentes,Alumnos,Cursos

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Docentes
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Alumnos
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cursos
        fields = '__all__'


class CursoseSerializer(serializers.ModelSerializer):
    nameAlumno = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cursos
        fields = ['CursoName', 'nameAlumno']
