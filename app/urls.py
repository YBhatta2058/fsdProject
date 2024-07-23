from django.urls import path
from . import views

urlpatterns = [
    path('',views.StudentListView.as_view(),name = "students"),
    path('students/<int:pk>',views.DetailListView.as_view(),name = "detailView"),
    path('generateCSV/',views.generateCSV,name = "generateCSV"),
    path('generatePDF/',views.generatePDF,name = "generatePDF")
]