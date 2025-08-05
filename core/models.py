from django.db import models

class Student(models.Model):
    # Basic Student Information
    school_name = models.CharField(max_length=255) 
    full_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100, unique=True)
    admission_no = models.CharField(max_length=50, unique=True, blank=True, null=True)
    record_no = models.CharField(max_length=50, unique=True, blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    nationality = models.CharField(max_length=50, default="Unknown")

    religion = models.CharField(max_length=50, blank=True, null=True)
    caste = models.CharField(max_length=50, blank=True, null=True)
    sub_caste = models.CharField(max_length=50, blank=True, null=True)
    sc_st = models.BooleanField(default=False)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50, default="Unknown")

    taluk = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    aadhar_no = models.CharField(max_length=12, blank=True, null=True)
    sts_no = models.CharField(max_length=20, blank=True, null=True)

    # Parent/Guardian Details
    father_name = models.CharField(max_length=100)
    father_aadhar = models.CharField(max_length=12, blank=True, null=True)
    mother_name = models.CharField(max_length=100)
    mother_aadhar = models.CharField(max_length=12, blank=True, null=True)
    parent_contact = models.CharField(max_length=15, blank=True, null=True)
    parent_email = models.EmailField(blank=True, null=True)

    # Student Contact & Address
    student_contact = models.CharField(max_length=15, blank=True, null=True)
    student_email = models.EmailField(unique=True, blank=True, null=True)
    address_permanent = models.TextField()
    address_temporary = models.TextField(blank=True, null=True)

    # Academic Details
    previous_school = models.CharField(max_length=150, blank=True, null=True)
    year_of_admission = models.IntegerField()
    year_of_graduation = models.IntegerField()
    course_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50, blank=True, null=True)
    current_semester = models.IntegerField()
    college_name = models.CharField(max_length=100)

    last_standard = models.CharField(max_length=100, blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    electives = models.TextField(blank=True, null=True)
    medium = models.CharField(max_length=50, blank=True, null=True)
    admission_date = models.DateField(blank=True, null=True)

    # Performance & Records
    cgpa = models.FloatField(blank=True, null=True)
    subjects_taken = models.TextField(blank=True, null=True)
    tenth_percentage = models.FloatField(blank=True, null=True)
    twelfth_percentage = models.FloatField(blank=True, null=True)

    # Fee & Scholarship Details
    fees_paid = models.BooleanField(default=False)
    scholarship_details = models.TextField(blank=True, null=True)
    fee_concessions = models.TextField(blank=True, null=True)

    # Attendance & Conduct
    last_attendance_date = models.DateField(blank=True, null=True)
    total_school_days = models.IntegerField(blank=True, null=True)
    days_attended = models.IntegerField(blank=True, null=True)
    character_conduct = models.CharField(max_length=100, blank=True, null=True)
    promotion_status = models.CharField(max_length=50, blank=True, null=True)
    medical_exam = models.BooleanField(default=False)

    # Transfer Certificate Issuance
    tc_application_date = models.DateField(blank=True, null=True)
    tc_issue_date = models.DateField(blank=True, null=True)
    tc_serial_no = models.CharField(max_length=20, unique=True, blank=True, null=True)  # Changed to CharField

    def save(self, *args, **kwargs):
        if self.tc_serial_no is None:  # Assign TC number only if not already set
            # Get the last serial number in the database and increment by 1
            last_tc = Student.objects.order_by('-tc_serial_no').first()
            
            # Extract the last number and increment it
            if last_tc and last_tc.tc_serial_no:
                # Extract number from the last serial (e.g., 001, 002, etc.)
                last_number = int(last_tc.tc_serial_no.split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1

            # Format the new serial number as 'TC-2025-001', 'TC-2025-002', etc.
            self.tc_serial_no = f"TC-2025-{new_number:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.student_id}) - TC No: {self.tc_serial_no}"
