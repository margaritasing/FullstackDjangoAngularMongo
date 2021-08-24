from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from InstitutoApp.models import Docentes,Alumnos,Cursos
from InstitutoApp.serializers import  DocenteSerializer,AlumnoSerializer,CursoSerializer,CursoseSerializer


from django.core.files.storage import default_storage


#@csrf_exempt
#@
#def docenteApi(request, pk):
    # ... tutorial = Tutorial.objects.get(pk=pk)
@csrf_exempt
def docenteApis(request,id=0):
    if request.method == 'GET':
        docentes = Docentes.objects.get(DocenteId=id)
        docentes_serializer=DocenteSerializer(docentes)
        return JsonResponse(docentes_serializer.data,safe=False)
    elif request.method == 'POST':
        docente_data = JSONParser().parse(request)
        docente_serializer = DocenteSerializer(data=docente_data)
        if docente_serializer.is_valid():
            docente_serializer.save()
            return JsonResponse(docente_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(docente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def docenteApi(request,id=0):
    if request.method=='GET':
        docentes = Docentes.objects.all()
        docentes_serializer=DocenteSerializer(docentes,many=True)
        return JsonResponse(docentes_serializer.data,safe=False)
    elif request.method == 'POST':
        docente_data=JSONParser().parse(request)
        docentes_serializer = DocenteSerializer(data=docente_data)
        if docentes_serializer.is_valid():
            docentes_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        docente_data=JSONParser().parse(request)
        docente=Docentes.objects.get(DocenteId=docente_data['DocenteId'])
        docentes_serializer=DocenteSerializer(docente,data=docente_data)
        if docentes_serializer.is_valid():
            docentes_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        docente=Docentes.objects.get(DocenteId=id)
        docente.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def alumnoApis(request,id=0):
    if request.method == 'GET':
        alumnos = Alumnos.objects.get(AlumnoId=id)
        alumnos_serializer=AlumnoSerializer(alumnos)
        return JsonResponse(alumnos_serializer.data,safe=False)

@csrf_exempt
def alumnisApi(request,id=0):
    if request.method == 'GET':
        alumnos = Cursos.objects.get(CursoId=id)
        alumnos_serializer=CursoseSerializer(alumnos)
        return JsonResponse(alumnos_serializer.data, safe=False)
  
@csrf_exempt
def alumnoApi(request,id=0):
    if request.method=='GET':
        alumnos = Alumnos.objects.all()
        alumnos_serializer=AlumnoSerializer(alumnos,many=True)
        return JsonResponse(alumnos_serializer.data,safe=False)
    elif request.method=='POST':
        alumno_data=JSONParser().parse(request)
        alumnos_serializer=AlumnoSerializer(data=alumno_data)
        if alumnos_serializer.is_valid():
            alumnos_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        alumno_data=JSONParser().parse(request)
        alumno=Alumnos.objects.get(AlumnoId=alumno_data['AlumnoId'])
        alumnos_serializer=AlumnoSerializer(alumno,data=alumno_data)
        if alumnos_serializer.is_valid():
            alumnos_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        alumno=Alumnos.objects.get(AlumnoId=id)
        alumno.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def cursoApis(request,id=0):
    if request.method == 'GET':
        cursos = Cursos.objects.get(CursoId=id)
        cursos_serializer=CursoSerializer(cursos)
        return JsonResponse(cursos_serializer.data,safe=False)
  
@csrf_exempt
def cursoApi(request,id=0):
    if request.method=='GET':
        cursos = Cursos.objects.all()
        cursos_serializer=CursoSerializer(cursos,many=True)
        return JsonResponse(cursos_serializer.data,safe=False)
    elif request.method=='POST':
        curso_data=JSONParser().parse(request)
        cursos_serializer=CursoSerializer(data=curso_data)
        if cursos_serializer.is_valid():
            cursos_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        curso_data=JSONParser().parse(request)
        curso=Cursos.objects.get(CursoId=curso_data['CursoId'])
        cursos_serializer=CursoSerializer(curso,data=curso_data)
        if cursos_serializer.is_valid():
            cursos_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        curso=Cursos.objects.get(CursoId=id)
        curso.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def saveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)
