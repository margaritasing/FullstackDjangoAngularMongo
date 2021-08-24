from django.db import models

class Cursos(models.Model):
    CursoId = models.AutoField(primary_key=True)
    CursoName = models.CharField(max_length=500)
   
    
    
class Alumnos(models.Model):
    AlumnoId = models.AutoField(primary_key=True)
    AlumnoName = models.CharField(max_length=50)
    Documento = models.CharField(max_length=50, default="Some String")
    DateOfJoining = models.DateField()
    Note= models.CharField(max_length=10, default="Some String")
    PhotoFileName = models.CharField(max_length=100)
    curso = models.ForeignKey(Cursos, related_name='nameAlumno', default=123, on_delete=models.CASCADE)

#Ya hice las migraciones, toca probar el endpoint... 
      
    class Meta:
        unique_together = ['curso', 'AlumnoId']
        ordering = ['AlumnoId']

    def __str__(self):
        return '%d: %s' % (self.AlumnoId, self.AlumnoName)

    

class Docentes(models.Model):
    DocenteId = models.AutoField(primary_key=True)
    DocenteName = models.CharField(max_length=50)
    Documento = models.CharField(max_length=50, default="Some String")
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
    curso=models.ForeignKey(Cursos,null=True, on_delete=models.CASCADE)
    alumno= models.ForeignKey(Alumnos,null=True, on_delete=models.CASCADE)
    
 

   



  #  alumno = models.ManyToManyField('self')
  #  related = models.ManyToManyField('self')
   



# Create your models here.
