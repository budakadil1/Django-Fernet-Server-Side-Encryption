# Django-Fernet-Server-Side-Encryption
## Django Fernet encryption/decryption

* This Project uses Python's cryptography.fernet Fernet module to encrypt and decrypt inputs.

the /encrypt page encrypts the input, returns it with the key used to encrypt it.

the /decrypt page decrypts the input (provided the right key) , not returning the key as the user should already have it.

There are no models used as no user data should be saved, everything (including Encryption/Decryption) is handled with forms.py and views.py.
