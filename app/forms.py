from django import forms
from django.core import validators
def validate1(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('name should not startswith a')
def validate2(name):
    if len(name)<=5:
        raise forms.ValidationError('length must be 5')
class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate1,validate2])
    sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    url=forms.URLField()
    botcatcher=forms.CharField(widget= forms.HiddenInput, required=False)
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if e!=re:
            raise forms.ValidationError('not matched')
    def cleaned_botcatcher(self):
        bot=self.cleaned_data.get('botcatcher')
        if len(bot)>0:
            raise forms.ValidationError('data entered by human')
