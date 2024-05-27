from django.urls import path
from .views import CompanyListView

urlpatterns = [
    path('api', CompanyListView.as_view(), name='company-list'),
]
