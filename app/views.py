from email.policy import default
from re import template
from django.shortcuts import render
from .models import Student
from django.views.generic import ListView
# Create your views here.
class StudentView(ListView):
    model = Student
    template_name = 'home.html'
    # template_name_suffix = '_get'==> it is _list by default 
    ordering = ['course']
    # context_object_name = 'students'==>we can give our own context object name

    def get_queryset(self):
        return Student.objects.filter(course='python')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['fresher'] = Student.objects.all().order_by('name')
        return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'loki':
    #         template_name = 'loki.html'
    #     else:
    #         template_name = self.template_name
    #     return super().get_template_names()

    def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = 'superuser.html'
        elif self.request.user.is_staff:
            template_name = 'staff.html'
        else:
            template_name = self.template_name
        return [template_name]
        