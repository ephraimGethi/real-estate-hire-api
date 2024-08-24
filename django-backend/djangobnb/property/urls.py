from django.urls import path
from . import api



urlpatterns = [
    path('',api.properties_list,name='api_properties_list'),
    path('create/',api.create_property,name='api_create_property'),
    path('<uuid:pk>',api.properties_detail,name='api_properties_detail'),
    path('<uuid:pk>/book/',api.book_property,name='api_properties_book'),
    path('<uuid:pk>/reservations/',api.property_reservation,name='api_property_reservations'),
    path('<uuid:pk>/toogle_favourite/',api.toggle_favourite,name='api_toogle_favourite'),
]
