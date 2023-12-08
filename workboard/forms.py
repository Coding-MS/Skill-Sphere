from django import forms
from django.forms import ModelForm
from .models import Workboard


class WorkboardForm(forms.ModelForm):
    """Create or edit a workboard."""

    class Meta:
        model = Workboard
        fields = [
            'title',
            'speciality',
            'start_date',
            'end_date',
            'description',
            'special_requests',
        ]

        # Use a custom widget for the start_date and end_date fields.
        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'},
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'},
            ),
        }


class WorkboardUpdateForm(forms.ModelForm):
    """Update a workboard."""

    class Meta:
        model = Workboard
        fields = [
            'title',
            'speciality',
            'start_date',
            'end_date',
            'description',
            'special_requests',
        ]

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class WorkboardDeleteForm(forms.ModelForm):
    """Delete a workboard."""

    class Meta:
        model = Workboard
        fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget = forms.HiddenInput()
