from django.dispatch import receiver
from django.db.models.signals import post_save
from proposals.tasks import analyze_proposal
from .models import Proposal


@receiver(post_save, sender=Proposal)
def send_to_analysis(sender, instance, created, **kwargs):
	if created:
		analyze_proposal.delay(instance.id)