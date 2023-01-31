from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # vamos herdar da usercreationform para criarmos a UserRegisterForm

class UserRegisterForm(UserCreationForm): #herdando da usercreationform
    #crio essa classe nova para modificar de acordo com o que eu quero
    email = forms.EmailField() # aqui eu crio um novo campo de email

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2'] #aqui são os campos que serão criados sempre que eu chamar a UserCreationForm