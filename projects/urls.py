#django rest framework tiene un modulo que nos crea todas las rutas basicas o el crud de estos datos
from rest_framework import routers
from .api import ProjectsViewSet

router = routers.DefaultRouter() #DefaultRouter es el modulo que crea el crud

router.register('api/projects', ProjectsViewSet, 'projects') #registro las urls

urlpatterns = router.urls #genera las urls