from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):  # aqui utilizaremos o forms.Form pois os campos do formulário não virão de um models
	username = forms.CharField(max_length=100, label='Username')
	password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)

	# método clean para apagar os dados de login quando mudar de página
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)

			if not user:
				raise forms.ValidationError('Usuário ou senha incorretos!')
			return super(LoginForm, self).clean()
