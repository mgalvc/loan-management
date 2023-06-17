from django.contrib import admin
from .models import Proposal, ProposalField


@admin.register(ProposalField)
class ProposalFieldAdmin(admin.ModelAdmin):
	list_display = ['field_name', 'enabled']


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
	list_display = ['id', 'status', 'created_at', 'updated_at']
	fields = ['status', 'metadata', 'created_at', 'updated_at']
	
	def has_add_permission(self, *args):
		return False
	
	def has_change_permission(self, *args):
		return False
	
	def has_delete_permission(self, *args):
		return False