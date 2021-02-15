from django.urls import path
from .views import (
    LeadDetailView, LeadCreateView, LeadListView, LeadUpdateView, LeadDeleteView
)
# required to provide an app name in order to be included in django main urls
app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete', LeadDeleteView.as_view(), name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
]
