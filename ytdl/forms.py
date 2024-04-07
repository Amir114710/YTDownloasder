from django import forms

class SearchItem(forms.Form):
    url = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':' تلفن همراه' , 'style':'text-align: left!important;'}),