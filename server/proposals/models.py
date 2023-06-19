from django.db import models
from django.utils.translation import gettext_lazy as _


class ProposalField(models.Model):
    
	field_name = models.CharField(max_length=200, verbose_name='Nome')
	enabled = models.BooleanField(default=True, verbose_name='Habilitado')

	def __str__(self) -> str:
		return self.field_name
	
	class Meta:
		verbose_name = 'Campo'
    

class Proposal(models.Model):
    
	class Status(models.TextChoices):
		PENDING = 'P', _('Pendente')
		APPROVED = 'A', _('Aprovado')
		DENIED = 'D', _('Negado')
		
	status = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=1)
	metadata = models.JSONField(verbose_name='Campos')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
	def __str__(self) -> str:
		return f'ID - {self.id}'
	
	class Meta:
		verbose_name = 'Proposta'

