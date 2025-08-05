from django import forms
from .models import Student

class StudentPersonalForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'school_name', 'full_name', 'student_id', 'date_of_birth', 'gender', 'nationality', 
            'religion', 'caste', 'sub_caste', 'state', 'district', 'taluk', 'blood_group', 
            'contact_number', 'place_of_birth', 'email', 'aadhar_no', 'sts_no', 
            'father_name', 'father_aadhar', 'mother_name', 'mother_aadhar', 
            'parent_contact', 'parent_email', 'student_contact', 'student_email', 
            'address_permanent', 'address_temporary', 'admission_no', 'record_no', 'sc_st'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter Contact Number'}),
            'address_permanent': forms.Textarea(attrs={'rows': 2}),
            'address_temporary': forms.Textarea(attrs={'rows': 2}),
        }

class StudentAcademicForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'previous_school', 'year_of_admission', 'year_of_graduation', 'course_name',
            'branch', 'current_semester', 'college_name', 'last_standard', 'languages',
            'electives', 'medium', 'admission_date'
        ]
        widgets = {
            'year_of_admission': forms.NumberInput(attrs={'min': 2000, 'max': 2100}),
            'year_of_graduation': forms.NumberInput(attrs={'min': 2000, 'max': 2100}),
            'admission_date': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget
        }

class StudentPerformanceForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'cgpa', 'subjects_taken', 'tenth_percentage', 'twelfth_percentage',
            'fees_paid', 'scholarship_details', 'fee_concessions', 'promotion_status',
            'last_attendance_date', 'total_school_days', 'days_attended',
            'character_conduct', 'tc_application_date', 'tc_issue_date', 'medical_exam'
        ]
        widgets = {
            'last_attendance_date': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget
            'tc_application_date': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget
            'tc_issue_date': forms.DateInput(attrs={'type': 'date'}),  # Calendar widget
            'cgpa': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 10}),
            'tenth_percentage': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 100}),
            'twelfth_percentage': forms.NumberInput(attrs={'step': '0.01', 'min': 0, 'max': 100}),
        }
