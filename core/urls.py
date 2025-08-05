from django.urls import path
from .views import (
    Home, LoginView, SignupView, DeleteStudentView, EditStudentView, LogoutView, samjo_page, StudentWizard,
    transfer_certificate, study_page,noc_page
)
from .forms import StudentPersonalForm, StudentAcademicForm, StudentPerformanceForm
from .views import students_form
from .views import DashboardView
from . import views


urlpatterns = [
    path('', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/<str:course>/', views.Home.as_view(), name='home'),  # For course only
    path('home/<str:course>/<str:semester>/', views.Home.as_view(), name='home'),     
     path('logout/', LogoutView.as_view(), name='logout'),
    path('delete-student/', DeleteStudentView.as_view(), name='delete_student'),
    path('edit-student/<int:id>/', EditStudentView.as_view(), name='edit_student'),
    path('samjo/<int:student_id>/', samjo_page, name='samjo_page'),
    
    # Multi-step form for adding students
    path('add-student/', StudentWizard.as_view([StudentPersonalForm, StudentAcademicForm, StudentPerformanceForm]), name='add_student'),
    
    path('transfer-certificate/<int:student_id>/', transfer_certificate, name='transfer_certificate'),
    path('students_form/<int:student_id>', students_form, name='students_form'),
    path('study/<int:student_id>/', study_page, name='study_page'),
     path('noc/<int:student_id>/', noc_page, name='noc_page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

     
     ]
