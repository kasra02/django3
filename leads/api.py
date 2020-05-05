from leads.serializers import LeadSerializer
from rest_framework import viewsets, permissions
from .models import Lead


# Lead Veiwset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
