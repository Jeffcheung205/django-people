from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from django.views.generic import ListView

from .models import Student, People



# Create your views here.
class LandingView(CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'demo_app/landing.html')

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'demo_app/student.html'

class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('demo_app:student')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('demo_app:student')

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('demo_app:student')

class PeopleListView(ListView):
    model = People
    context_object_name = 'people'
    template_name = 'demo_app/people.html'

class PeopleDetailView(DetailView):
    model = People
    context_object_name = 'people'
    template_name = 'demo_app/people.html'

class PeopleUpdateView(UpdateView):
    model = People
    fields = '__all__'
    success_url = reverse_lazy('demo_app:people')

class PeopleDeleteView(DeleteView):
        model = People
        context_object_name = 'people'
        success_url = reverse_lazy('demo_app:people')

