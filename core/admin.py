from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id','full_name', 'student_id', 'date_of_birth', 'gender', 'nationality', 
        'religion', 'caste', 'sub_caste', 'state', 'district', 'taluk', 
        'blood_group', 'contact_number', 'place_of_birth', 'email',
        'father_name', 'father_aadhar', 'mother_name', 'mother_aadhar', 
        'parent_contact', 'parent_email', 'student_contact', 'student_email',
        'address_permanent', 'address_temporary', 
        'previous_school', 'year_of_admission', 'year_of_graduation', 
        'course_name', 'branch', 'current_semester', 'college_name',
        'cgpa', 'subjects_taken', 'tenth_percentage', 'twelfth_percentage',
        'fees_paid', 'scholarship_details', 'fee_concessions', 'last_attendance_date',
        'total_school_days', 'days_attended', 'character_conduct', 'tc_application_date', 'tc_issue_date',
        
        # ✅ Adding missing fields
        'school_name', 'admission_no', 'record_no', 'aadhar_no', 'sts_no',
        'sc_st', 'promotion_status', 'last_standard', 'languages', 'electives',
        'medium', 'admission_date', 'medical_exam'
    ]

    search_fields = ['full_name', 'student_id', 'email', 'father_name', 'mother_name', 'parent_contact', 'admission_no', 'record_no']  
    list_filter = ['gender', 'nationality', 'state', 'district', 'course_name', 'year_of_admission', 'fees_paid', 'medium']  
    ordering = ['student_id']  
    list_per_page = 20  

admin.site.register(Student, StudentAdmin)
