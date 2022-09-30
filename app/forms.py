from dataclasses import fields
from django.forms  import ModelForm
from .models import Patient

class patientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'phone', 'email', 'age', 'gender', 'description']

    def __init__(self, *args, **kwargs):
        super(patientForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})