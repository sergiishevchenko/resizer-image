from django import forms

class UploadFileForm(forms.Form):
    url = forms.CharField()
    file = forms.ImageField()
