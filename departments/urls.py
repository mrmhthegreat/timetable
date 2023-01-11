from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 
urlpatterns = [
    path('',views.allocationform,name='depart'),
    path('program/',views.programs,name='program'),
    path('samester/',views.samester,name='samester'),
    path('course/',views.courser,name='course'),
    path('fill/',views.fill,name='fill'),
    path('cj/',views.courserj,name='cj'),

    
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
