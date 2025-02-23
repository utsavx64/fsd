from django.urls import path
from .views import home_view, ComplaintCreateView
from django.views.generic import TemplateView

urlpatterns = [
    path('', home_view, name='home'),
    path('submit/', ComplaintCreateView.as_view(), name='submit_complaint'),
    path('success/', TemplateView.as_view(
        template_name='complaints/success.html'),
        name='complaint_success'
    ),
]