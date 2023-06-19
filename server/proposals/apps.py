from django.apps import AppConfig


class ProposalsConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'proposals'
	verbose_name = 'Propostas de Empréstimo'
	
	def ready(self):
		import proposals.signals
