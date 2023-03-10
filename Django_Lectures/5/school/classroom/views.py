from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import ContactForm
from django.urls import reverse, reverse_lazy
from .models import Teacher
# Create your views here.


class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    # model_form.html
    # .save()
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')

class TeacherListView(ListView):
    model = Teacher
    # model_list.html
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = 'teacher_list'

class TeacherDeatilView(DetailView):
    # Return only one model entry pk
    # model_detail.html
    model = Teacher
    # pk --> {{teacher}}
class TeacherUpdateView(UpdateView):
    # Share model_form.html --- PK
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')

class TeacherDeleteView(DeleteView):
    # Form --> Confirm Delete Button
    # default template name:
    # model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    #success url?
    #success_url = "/classroom/thank_you/"
    success_url = reverse_lazy('classroom:thank_you')

    #what to do with the form?
    def form_valid(self, form):
        print(form.cleaned_data)
        #ContactForm(request.POST)
        return super().form_valid(form)