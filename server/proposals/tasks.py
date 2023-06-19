from time import sleep
from proposals.models import Proposal
from celery import shared_task
import random


@shared_task()
def analyze_proposal(proposal_id):
	# Wait 10s to simulate a time intensive task
	sleep(10)

	# Gets a random status for testing purposes
	status = random.choice((Proposal.Status.APPROVED, Proposal.Status.DENIED))

	# Find the proposal and set its status
	proposal = Proposal.objects.get(pk=proposal_id)
	proposal.status = status
	proposal.save()