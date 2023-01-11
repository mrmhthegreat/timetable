from django.db import models

# Create your models here.

class Department(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True)
    department_name = models.CharField(max_length=200)
    total_student=models.IntegerField()
    total_room=models.IntegerField()
    total_labs=models.IntegerField()
    def save(self, *args, **kwargs):
        
        self.short_name=self.short_name.capitalize()
        super(Department, self).save(*args, **kwargs)

    def __str__(self):
        return self.department_name.capitalize()
    
class Program(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True)
    program_name = models.CharField(max_length=200)
    currently_available_sms=models.CharField(max_length=200)
    total_students=models.IntegerField()
    department_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        
        self.short_name=self.short_name.capitalize()
        super(Program, self).save(*args, **kwargs)

    def __str__(self):
        return self.program_name.capitalize()

class Room(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True)
    block_name = models.CharField(max_length=200)
    total_seats=models.IntegerField()
    department_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    is_smart_room=models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        
        self.short_name=self.short_name.capitalize()
        super(Room, self).save(*args, **kwargs)
    def __str__(self):
        return self.department_id.short_name.capitalize()+" " +self.short_name.capitalize()

class Lab(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True)
    block_name = models.CharField(max_length=200)
    total_seats=models.IntegerField()
    department_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    is_smart_lab=models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        
        self.short_name=self.short_name.capitalize()
        super(Lab, self).save(*args, **kwargs)
    def __str__(self):
        return self.department_id.short_name+" " +self.short_name.capitalize()

class Teacher(models.Model):
    teacher_id=models.CharField(unique=True,max_length=200,primary_key=True)
    full_name = models.CharField(max_length=200)
    department_id=models.ForeignKey(Department, on_delete=models.CASCADE)
    designation=models.CharField(default="Leacturer",max_length=200,choices=(('Leacturer',"Leacturer"),('Assistante_Professor','Assistante Professor'),("Associate_Prfessor","Associate Prfessor"),("Professor","Professor")))
    additional_duties=models.IntegerField(null=True)
    teacher_qulification = models.CharField(max_length=200,null=True,)
    have_freezing_slot=models.BooleanField(default=False)
    freezing_slot_start=models.TimeField()
    freezing_slot_end=models.TimeField()
    def __str__(self):
        return self.full_name.capitalize()

class Prerequest(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True)
    course_name = models.CharField(max_length=200)
    credits_hourse=models.IntegerField()
    def save(self, *args, **kwargs):
        
        self.short_name=self.short_name.upper()
        super(Prerequest, self).save(*args, **kwargs)
    def __str__(self):
        return self.short_name.capitalize() 
     
class Course(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True,help_text=" courser Code It Must be unique")
    course_name = models.CharField(max_length=200)
    credits_hourse=models.IntegerField()
    classes_per_week=models.IntegerField()
    prerequest_id=models.ForeignKey(Prerequest, on_delete=models.CASCADE,blank=True,null=True,help_text="only if course have pre request")
    classes_per_week=models.IntegerField()
    have_labs=models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        
        self.short_name=self.short_name.upper()
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.short_name.upper()

class course_and_teacher(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True,editable=False)
    teacher_id=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    section_id=models.ForeignKey('Samester_and_Section', on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        
        self.short_name=self.section_id.short_name.capitalize() + " Course " +self.course_id.short_name.upper()+ "  By " +self.teacher_id.full_name.capitalize()
        super(course_and_teacher, self).save(*args, **kwargs)

    def __str__(self):
        return self.short_name

class Samester_and_Section(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True)
    samester=models.CharField(max_length=200,choices=(("1st","1st"),("2nd","2nd"),("3rd","3rd"),("4th","4th"),("5th","5th"),("6th","6th"),("7th","7th"),("8th","8th"),("9th","9th"),("10th","10th"),("11th","11th"),("12th","12th")),default='1st')
    sections=models.CharField(max_length=200,choices=(("A","A"),("B","B"),("C","C"),("D","D"),("E","E")),default='A')
    program_id=models.ForeignKey(Program, on_delete=models.CASCADE)
    student_strength=models.IntegerField()
    is_available=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        
        self.short_name=self.program_id.short_name.upper() + "  " +self.samester + "  " +self.sections
        super(Samester_and_Section, self).save(*args, **kwargs)

    def __str__(self):
        return self.short_name


# class Section(models.Model):
#     short_name=models.CharField(unique=True,max_length=200,primary_key=True)
#     student_strength=models.IntegerField()
#     def __str__(self):
#         return self.short_name.capitalize()



# class Samester(models.Model):
#     short_name=models.CharField(unique=True,max_length=200,primary_key=True)
#     is_available=models.BooleanField(default=False)
#     def __str__(self):
#         return self.short_name.capitalize()


class AllocationForm(models.Model):
    roll_number=models.CharField(unique=True,max_length=200,primary_key=True)
    email= models.EmailField(null=True)
    full_name = models.CharField(max_length=200)
    section=models.CharField(max_length=200,default="A",choices=(('A','A'),('B','B'),('C','C')))
    courses_ids=models.ManyToManyField(Course,related_name="course")
    program_id=models.OneToOneField(Course,on_delete=models.CASCADE,null=True)
    # samester_id=models.OneToOneField(Samester, on_delete=models.CASCADE)
    department_id=models.OneToOneField(Department, on_delete=models.CASCADE,null=True)

    is_available=models.BooleanField(default=False)
    def __str__(self):
        return self.short_name.capitalize()

from django import forms
class ModelAllocationForm(forms.ModelForm):
    class Meta:
        model=AllocationForm
        fields="__all__"
    