from django.db import models

from departments.models import Department, Lab, Room, course_and_teacher

# Create your models here.
class TimeTable(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True)
    department_id=models.OneToOneField(Department, on_delete=models.CASCADE)
    room_id=models.OneToOneField(Room, on_delete=models.CASCADE,null=True)
    lab_id=models.OneToOneField(Lab, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.short_name.capitalize()

class TimeTable_Slot(models.Model):
    short_name=models.CharField(unique=True,max_length=200,primary_key=True)
    # room_id=models.OneToOneField(Room, on_delete=models.CASCADE)
    # lab_id=models.OneToOneField(Lab, on_delete=models.CASCADE)
    course_and_teacher_id=models.OneToOneField(course_and_teacher, on_delete=models.CASCADE)
    weekday=models.CharField(default="Monday",max_length=200,choices=(('Monday',"Monday"),('Tuesday','Tuesday'),("Wednesday","Wednseday"),("Thursday","Thurdasy"),("Firday","Friday")))
    start_time=models.TimeField()
    end_time=models.TimeField()
    def __str__(self):
        return self.full_name.capitalize()