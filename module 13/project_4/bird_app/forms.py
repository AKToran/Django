from django import forms 
from django.core import validators


# * forms holo form api

#* widgets == fields to html input. view page source e giye sob dhore dhore change kora jabe

class contactForm(forms.Form):
    name = forms.CharField(label='Full Name:', help_text="Enter your full name.",
                           widget= forms.Textarea(attrs={'id': 'full_name', 'class': 'class class2', 'placeholder': 'Enter your full name', 'rows': "4"}))

    # * initial: empty rakhle eta bosai dibe.
    # nick_name = forms.CharField(label='Nick_Name:', initial="Motka", disabled=True)
    


    # file = forms.FileField(required=False) 
    # image = forms.ImageField(required=False)
    #* file er jonno dj forms e: enctype="multipart/form-data" views.py e contactForm e request.Files add korte hobe. 

    # email = forms.EmailField(label='Email Address')
    # age = forms.IntegerField(required=False)
    # weight = forms.FloatField(required=False)
    # balance = forms.DecimalField(required=False)
    # age = forms.CharField(widget=forms.NumberInput)
    # check = forms.BooleanField(required=False, label='Agree to our terms and conditions')
    # birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(required=False, widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    # appoint = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # #* list of tuples. (backend data, frontend show)
    size = forms.ChoiceField(choices= CHOICES, required=False, widget=forms.RadioSelect) 
    TOPPINGS = [('P', 'Pepperoni'), ('C','Chicken'), ('B','Beef'), ('O','onion')]
    pizza = forms.MultipleChoiceField(choices= TOPPINGS, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 5:
#     #         raise forms.ValidationError("Enter at least 5 characters")
#     #     else:
#     #         return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Please enter a valid email address")
#     #     else:
#     #         return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']

#         if len(valname) < 5:
#             raise forms.ValidationError("Enter at least 5 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Please enter a valid email address")

 
def lenCheck(value):
    if len(value) < 10:
        raise forms.ValidationError("Please enter at least 10 characters")

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, 
                           validators=[validators.MinLengthValidator(5,  message= "enter at least 5 characters")])
    

    text = forms.CharField(widget=forms.TextInput, validators=[lenCheck])

    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email address")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(50, message="too old"), validators.MinValueValidator(10, message="tooooo young")])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message = 'enter a valid file')])
    # * regex, url....



class passwordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_con_pass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_pass != val_con_pass:
            raise forms.ValidationError("Passwords do not match")
        if len(val_name) > 20:
            raise forms.ValidationError("too long name")
            
        