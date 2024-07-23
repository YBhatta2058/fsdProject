from django.urls import path
from .views import *

urlpatterns = [
    path('form/',myView,name = 'form'),
    path('successful/',successView,name = 'success'),
    path('listOfStudents/',listOfStudents,name = 'list')
]
