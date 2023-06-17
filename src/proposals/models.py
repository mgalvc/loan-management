from django.db import models
from django.utils.translation import gettext_lazy as _


class ProposalField(models.Model):
    
	field_name = models.CharField(max_length=200)
	enabled = models.BooleanField(default=True)

	def __str__(self) -> str:
		return self.field_name
    

class Proposal(models.Model):
    
	class Status(models.TextChoices):
		PENDING = 'P', _('Pending')
		APPROVED = 'A', _('Approved')
		DENIED = 'D', _('Denied')
		
	status = models.CharField(choices=Status.choices, default=Status.PENDING, max_length=1)
	metadata = models.JSONField(verbose_name='Fields')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    
	def __str__(self) -> str:
		return f'ID - {self.id}'

