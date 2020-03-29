# Django-Fernet-Server-Side-Encryption
Django Fernet encryption/decryption

* This Project uses Python's cryptography.fernet Fernet module to encrypt and decrypt inputs.

the /encrypt page encrypts the input, returns it with the key used to encrypt it.

the /decrypt page decrypts the input (provided the right key) , not returning the key as the user should already have it.
