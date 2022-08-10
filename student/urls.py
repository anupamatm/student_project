from django.urls import path
from .import views

urlpatterns=[
   
   path('about/',views.about, name='about'),
   path('contact/',views.contact, name='contact'),
   path('login/',views.login, name='login'),
   path('marks/',views.marks, name='marks'),
   path('studentview/',views.views_student, name='views_student'),
   path('attendenceview/',views.views_attendence, name='views_attendence'),

]