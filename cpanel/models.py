from django.db import models

#modelo de cadastro
class RegistrationData (models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    atuacao = models.CharField(max_length=100)
    
#retorna variavel nome para exibição no painel de administração django
    def __str__(self):
        return self.nome