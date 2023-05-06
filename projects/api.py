#el viewset nos permite conocer quien puede consultar la api, que peticiones se pueden hacer o si se necesita algun tipo de autenticacion

from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectsSerializers

class ProjectsViewSet(viewsets.ModelViewSet):
    #indicamos que consultas se pueden hacer
    queryset = Project.objects.all() #mi conjunto de datos
    permission_classes = [permissions.AllowAny] #cualquier cliente puede solicitar datos
    serializer_class = ProjectsSerializers #a parti de que serializador usa los datos
    
