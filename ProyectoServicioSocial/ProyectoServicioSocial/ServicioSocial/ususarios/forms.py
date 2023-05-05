from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'repassword')

    username = forms.CharField(max_length=50, required=True)
    
    email = forms.EmailField(required=True)
    
    password = forms.CharField(
        min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    repassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # Encripta la contraseña
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    # Valida que el correo no se repita en varios registros
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('El email ya se encuentra registrado en otra cuenta, ingrese uno diferente')
        return email

    # Valida que las contraseñas ingresadas sean iguales
    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['repassword']:
            raise forms.ValidationError(
                'Las contraseñas son diferentes, favor de verificar')
        return self.data['password']
