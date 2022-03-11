from django.urls import path
from tickets import views

urlpatterns = [
    path('tickets/list-all',views.tickets_list),
    path('tickets/add-ticket',views.add_single_ticket),
    path('tickets/get-last-ticket',views.last_ticket),
    path('tickets/classify-ticket/<int:pk>',views.classify_ticket),
]