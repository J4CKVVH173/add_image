from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    file = forms.FileField(label='File' )
    file1 = forms.FileField(label='File2')
    file2 = forms.FileField(label='File1')