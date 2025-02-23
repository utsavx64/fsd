from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Complaint
from .forms import ComplaintForm

def home_view(request):
    return render(request, 'complaints/home.html')

class ComplaintCreateView(CreateView):
    model = Complaint
    form_class = ComplaintForm
    template_name = 'complaints/complaint_form.html'
    success_url = reverse_lazy('complaint_success')

# Create your views here.

