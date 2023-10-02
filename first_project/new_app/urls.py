from django.urls import path
from .views import index,contact,projects,resume


urlpatterns = [
    path('',index, name='indexd_page'),
    path('contact',contact, name='contact'),
    path('projects',projects, name='projects'),
    path('resume',resume, name='resume'),
    

]