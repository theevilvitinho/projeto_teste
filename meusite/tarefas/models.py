from django.db import models

# Create your models here.
class TarefaModel(models.Model):
    assunto = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.assunto