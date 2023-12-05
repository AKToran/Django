from django import forms
from first.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Student Name:',
            'roll' : 'Student Roll:',
            'father_name' : 'Father\'s Name:'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'bg-danger'}),
            # 'roll' : forms.PasswordInput(),
            'address' : forms.Textarea(attrs={'rows': 4})
        }
        help_texts = {
            'name' : 'Write Full Name',
            'father_name': 'Enter your father\'s name'
        }

        error_messages = {
            'name': { 'required' : 'Your name is required' },

        }
