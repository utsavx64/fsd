from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'product', 'description', 'priority']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }