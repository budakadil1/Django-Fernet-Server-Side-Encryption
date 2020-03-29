from django import forms

class DecryptInputForm(forms.Form):
    decrypt = forms.CharField(label='To Decrypt',max_length=1000)

class EncryptInputForm(forms.Form):
    encrypt = forms.CharField(label='To Encrypt',max_length=1000)

class FernetKeyForm(forms.Form):
    key = forms.CharField(label='Enter your Fernet Key right here:', max_length=1000)
