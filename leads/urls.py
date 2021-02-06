from django.urls import path
from leads.views import (lead_list, lead_detail, lead_create,
 lead_update, lead_delete, 
 LeadCreateView, LeadDeleteView, LeadDetailView, LeadUpdateView, LeadListView)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:id>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:id>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:id>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
]