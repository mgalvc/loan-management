from rest_framework import serializers, generics
from django.urls import path
from .models import ProposalField, Proposal


class ProposalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProposalField
        fields = ['field_name']
        

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['metadata']


class ProposalFieldListApiView(generics.ListAPIView):
    queryset = ProposalField.objects.filter(enabled=True)
    serializer_class = ProposalFieldSerializer
    

class ProposalCreateApiView(generics.CreateAPIView):
    serializer_class = ProposalSerializer
    

urlpatterns = [
    path('proposal-fields/', ProposalFieldListApiView.as_view()),
    path('proposals', ProposalCreateApiView.as_view())
]