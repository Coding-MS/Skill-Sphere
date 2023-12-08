from django import forms
from .models import Workboard

class WorkboardForm(forms.ModelForm):
    # SPECIALITIES = [
    #     ('Plumber','Plumber'),
    #     ('Caterers', 'Caterers'),
    #     ('Seamstress', 'Seamstress'),
    #     ('Hairdresser', 'Hairdresser'),
    #     ('Technical Repairs','Technical Repairs'),
    #     ('Legal', 'Legal'),
    #     ('Painter','Painter'),
    #     ('Other', 'Other'),
    # ]

    # title = forms.CharField(max_length=255, label='Title of the Post')
    # speciality = forms.ChoiceField(choices=SPECIALITIES, label='Speciality')
    # start_date = forms.DateField(label='Start Date')
    # end_date = forms.DateField(label='End Date')
    # description = forms.CharField(widget=forms.Textarea, label='Description of the Project')
    # special_requests = forms.CharField(widget=forms.Textarea, label='Special Requests/Requirements')

    class Meta:
        model = Workboard
        fields = ['title', 'speciality', 'start_date', 'end_date', 'description', 'special_requests']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
