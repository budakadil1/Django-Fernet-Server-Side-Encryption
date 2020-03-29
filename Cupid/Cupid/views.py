from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect


from .forms import EncryptInputForm, DecryptInputForm, FernetKeyForm
from cryptography.fernet import Fernet



## FUNCTION FOR '/encrypt'

def encrypt(request):
    key = Fernet.generate_key()
    user_token = key.decode()
    ## GET POST
    if request.method == 'POST':
        form = EncryptInputForm(request.POST)
        #CHECK IF FORM IS VALID
        if form.is_valid():
            #GET CLEANED DATA FROM TEXTAREA
            text = form.cleaned_data['encrypt']
            print(text)
        f = Fernet(key)
        #ENCODE TEXT
        text_encoded = text.encode()
        #ENCRYPT TEXT
        encrypted = f.encrypt(text_encoded)
        to_print = encrypted.decode()
        #CONSOLE PRINTS
        ##USER FRIENDLY KEY + ENCRYPTION PRINT
        key_user_friendly = key.decode()
        print(to_print)
        arguments = {'text':to_print,'text2':key_user_friendly, 'key_present':'Key:'}
        return render(request, 'result.html', arguments)
    else:
        #RETURN EMPTY FORM with placeholder text IF USER REQUEST = GET
        form = EncryptInputForm({'encrypt':'Enter some text here'})
    #RENDER + ARGUMENTS
    args = {'form':form}
    return render(request, 'encrypt.html', args)



## FUNCTION FOR '/decrypt'
## FIX STATIC FILES
def decrypt(request):
    ## GET POST REQUEST
    if request.method == 'POST':
        form = DecryptInputForm(request.POST)
        form2 = FernetKeyForm(request.POST)
        #CHECK IF FORM IS VALID
        if form.is_valid():
            #GET CLEANED TEXT INPUT FROM FORM
            text = form.cleaned_data['decrypt']
            #USER TEXT READABLE
            print(text)
            # ENCODE TEXT FROM STR TO BYTES SO FERNET CAN DO IT's MAGIC
            text_encoded = text.encode()
        #CHECK IF KEYFORM IS VALID
        if form2.is_valid():
            #GET CLEANED KEY FROM FORM
            key_decrypt= form2.cleaned_data['key']
        f = Fernet(key_decrypt)
        decrypted = f.decrypt(text_encoded)
        #USER FRIENDLY DECODE
        user_friendly_decode = decrypted.decode()
        print(decrypted)
        arguments = {'text':user_friendly_decode}
        return render(request, 'result.html', arguments)
    else:
        #RETURN EMPTY FORM with placeholder text if USER REQUEST = GET
        ## FERNET FORM IS NOT RETURNED AS NO KEY IS GENERATED FOR DECRYPT
        form = DecryptInputForm({'decrypt':'Enter some text here'})
    args = {'form':form, 'fernet_form':FernetKeyForm}
    return render(request, 'decrypt.html', args)
