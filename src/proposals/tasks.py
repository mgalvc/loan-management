from time import sleep
from proposals.models import Proposal
from celery import shared_task
import random


@shared_task()
def analyze_proposal(proposal_id):
	sleep(10)
	status = random.choice((Proposal.Status.APPROVED, Proposal.Status.DENIED))
	proposal = Proposal.objects.get(pk=proposal_id)
	proposal.status = status
	proposal.save()