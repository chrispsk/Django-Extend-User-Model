from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    city=forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'})) # Required
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta():
        model = User
        help_texts = {
            'username': None, # Make default message dissapear
        }
        fields = ('username','email', 'city', 'first_name', 'last_name', 'password')
        widgets = {
            'last_name': forms.Textarea(attrs={'cols': 20, 'rows': 1, 'class':"form-control form-control-lg"}),
        }

    # Password Confirm Password Validation
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password", "")
        confirm_password = cleaned_data.get("confirm_password", "")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        if len(password) < 4:
            raise forms.ValidationError('Password too short')

    def clean_city(self, *args, **kwargs):
        city = self.cleaned_data.get('city')
        if len(city) < 2:
            raise forms.ValidationError("City Too Short !!!!!")
        return city
