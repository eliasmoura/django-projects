from django import forms

class FormContato(forms.Form):
	nome = forms.CharField(max_length=50)
	107email = forms.EmailField(required=False)
	mensagem = forms.Field(widget=forms.Textarea)