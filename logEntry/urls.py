from django.urls import path
from . import views

app_name = 'entry'


urlpatterns = [
    path('entry/<user>/', views.entry_list, name='entry-list'),
    path('add-entry/', views.EntryCreateView.as_view(), name='add-entry'),
    path('entry/<int:pk>/', views.EntryDetailView.as_view(), name='entry-detail'),
]