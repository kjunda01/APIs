from django.db import models

class User(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    date_of_birth = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profession = models.CharField(max_length=250, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)  # Campo para foto de perfil

    def __str__(self):
        return self.name
