from django.urls import path
from leads.views import (lead_list, lead_detail, lead_create,
 lead_update, lead_delete, LeadList, LeadViewDetail, LeadCreate,
  LeadViewCreate, LeadViewDelete)

app_name = "leads"

urlpatterns = [
    path('', lead_list, name='lead-list'),
    path('<int:id>/', lead_detail, name='lead-detail'),
    path('<int:id>/update/', lead_update, name='lead-update'),
    path('<int:id>/delete/', lead_delete, name='lead-delete'),
    path('create/', lead_create, name='lead-create'),
]