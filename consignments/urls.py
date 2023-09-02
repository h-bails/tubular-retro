from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_consignment, name='new_consignment'),
    path('manage/', views.manage_consignments, name='manage_consignments'),
]
