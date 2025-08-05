from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Student
from .forms import StudentPersonalForm, StudentAcademicForm, StudentPerformanceForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages
from formtools.wizard.views import SessionWizardView
from .models import Student 
from django.http import Http404

# Signup View
class SignupView(View):
    def get(self, request):
        return render(request, 'core/signup.html')

    def post(self, request):
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')

        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists. Try a different one.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered. Try logging in.")
            return redirect('signup')

        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')


# Login View
class LoginView(View):
    def get(self, request):
        return render(request, 'core/signup.html')

    def post(self, request):
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username=uname, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')


# Home 
class Home(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, course=None, semester=None):
        # Define valid courses and semesters
        valid_courses = ['bca', 'bba', 'bcom']
        valid_semesters = ['1', '2', '3', '4', '5', '6']

        # Check if the course is valid
        if course and course not in valid_courses:
            raise Http404("Course not found")

        # Check if the semester is valid (only if semester is provided)
        if semester and semester not in valid_semesters:
            raise Http404("Semester not found")

        # Calculate total students for each course
        total_students_bca = Student.objects.filter(course_name='bca').count()
        total_students_bba = Student.objects.filter(course_name='bba').count()
        total_students_bcom = Student.objects.filter(course_name='bcom').count()

        # Adjusted to use current_semester and course_name for filtering
        if course and semester:
            # If both course and semester are provided, filter by both
            stu_data = Student.objects.filter(course_name=course, current_semester=semester)
        elif course:
            # If only course is provided, filter by course name
            stu_data = Student.objects.filter(course_name=course)
        else:
            # If no course is provided, show all students
            stu_data = Student.objects.all()

        # Get the total number of students after filtering
        total_students = stu_data.count()

        # Render the page with the filtered student data and total count
        return render(request, 'core/home.html', {
            'studata': stu_data,
            'course': course,
            'semester': semester,
            'total_students': total_students,
            'total_students_bca': total_students_bca,
            'total_students_bba': total_students_bba,
            'total_students_bcom': total_students_bcom,
        })





# Multi-Step Student Form View
class StudentWizard(SessionWizardView):
    form_list = [StudentPersonalForm, StudentAcademicForm, StudentPerformanceForm]
    template_name = "core/multi_step_form.html"

    def done(self, form_list, **kwargs):
        student = Student()
        for form in form_list:
            if form.is_valid():
                for field, value in form.cleaned_data.items():
                    setattr(student, field, value)
        student.save()
        messages.success(self.request, "Student record successfully added.")
        return redirect('home', course=student.course_name)


# Delete Student View
class DeleteStudentView(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request):
        student_id = request.POST.get('id')

        if not student_id:
            messages.error(request, "Student ID is required for deletion.")
            return redirect('home')
        student = get_object_or_404(Student, pk=student_id)

        student.delete()
        messages.success(request, "Student record deleted successfully.")
        return redirect('home', course=student.course_name)


# Edit Student View
class EditStudentView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        personal_form = StudentPersonalForm(instance=student)
        academic_form = StudentAcademicForm(instance=student)
        performance_form = StudentPerformanceForm(instance=student)
        return render(request, 'core/edit_student.html', {
            'personal_form': personal_form,
            'academic_form': academic_form,
            'performance_form': performance_form
        })

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        personal_form = StudentPersonalForm(request.POST, instance=student)
        academic_form = StudentAcademicForm(request.POST, instance=student)
        performance_form = StudentPerformanceForm(request.POST, instance=student)

        if personal_form.is_valid() and academic_form.is_valid() and performance_form.is_valid():
            personal_form.save()
            academic_form.save()
            performance_form.save()

            messages.success(request, "Student details updated successfully.")
            return redirect('home', course=student.course_name)

        messages.error(request, "There was an error updating the student details.")
        return render(request, 'core/edit_student.html', {
            'personal_form': personal_form,
            'academic_form': academic_form,
            'performance_form': performance_form
        })


# Logout View
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('login')


# Custom Student Detail View
def samjo_page(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'core/samjo.html', {'student': student})


# Transfer Certificate View
def transfer_certificate(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'core/transfer_certificate.html', {'student': student})

def students_form(request,student_id):
    stu = Student.objects.get(id=student_id)
    return render(request, 'core/student_form.html',{'stud':stu})

def study_page(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'core/study.html', {'student': student})

def noc_page(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'core/noc.html', {'student': student})

class DashboardView(View):
     def get(self, request):
        
        total_students_bca = Student.objects.filter(course_name='bca').count()
        total_students_bba = Student.objects.filter(course_name='bba').count()
        total_students_bcom = Student.objects.filter(course_name='bcom').count()


        return render(request, 'core/dashboard.html', {
            'total_students_bca': total_students_bca,
            'total_students_bba': total_students_bba,
            'total_students_bcom': total_students_bcom,})
     
      