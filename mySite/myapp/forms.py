from django import forms
from .models import studentInformationModel, dateOfCleanup
from django.forms import inlineformset_factory

class studentInformationForm(forms.ModelForm):
    class Meta:
        model = studentInformationModel
        fields = ['name', 'idNum', 'school', 'hours', 'cleanup']

class cleanUpDateForm(forms.ModelForm):
    class Meta:
        model = dateOfCleanup
        fields = ['date']

studentFormSet = inlineformset_factory(dateOfCleanup, studentInformationModel, form=studentInformationForm, extra=1, can_delete=True)
