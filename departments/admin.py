from django.contrib import admin

# Register your models here.
from .models import Department,Lab,Room,Program,Teacher,Course,AllocationForm,Prerequest,Samester_and_Section,course_and_teacher
admin.site.site_header = 'Centerlized TimeTable For Aust'


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("short_name", "department_name", "total_labs",'total_room')
    search_fields = ['department_name']


@admin.register(Lab)
class LabAdmin(admin.ModelAdmin):
    list_display = ("short_name", "department",'block_name', "total_seats")

    search_fields = ['department'] 
    def department(self, obj):
        if(obj.department_id):
            return obj.department_id.department_name 


        return 'No ' 
    department.admin_order_field  = 'department_1d'  #Allows column order sorting
    department.short_description = 'Department'  #Renames column head




@admin.register(Room)
class LabAdmin(admin.ModelAdmin):
    list_display = ("short_name", "department",'block_name', "total_seats")

    search_fields = ['department'] 
    def department(self, obj):
        if(obj.department_id):
            return obj.department_id.department_name 


        return 'No ' 
    department.admin_order_field  = 'department_1d'  #Allows column order sorting
    department.short_description = 'Department'  #Renames column head
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(Prerequest)
admin.site.register(AllocationForm)


@admin.register(Samester_and_Section)
class SmS(admin.ModelAdmin):
    readonly_fields = ["short_name"]
    list_display = ("short_name", "department", "student_strength",'is_available')
    list_filter = ['program_id__short_name','program_id__department_id__short_name']
    
    search_fields = ['program_id__short_name','program_id__department_id__short_name','program_id__department_id__department_name'] 
    def department(self, obj):
        if(obj.program_id):
            return obj.program_id.department_id.short_name 


        return 'No ' 
    department.admin_order_field  = 'program_id'  #Allows column order sorting
    department.short_description = 'Department' 
    
@admin.register(course_and_teacher)
class CourseandTecaherAdmin(admin.ModelAdmin):
    readonly_fields = ["short_name"]

    


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("short_name", "course_name", "have_labs",'prerequest')
    list_filter = ['have_labs']
    search_fields = ['course_name']
   
    def prerequest(self, obj):
        if(obj.prerequest_id):
            return obj.prerequest_id.short_name 


        return 'No ' 
    prerequest.admin_order_field  = 'prerequest_id'  #Allows column order sorting
    prerequest.short_description = 'Pre Request'  #Renames column head