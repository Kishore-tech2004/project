from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('book-tickets/', views.book_tickets, name='book_tickets'),
    path('view-booked-tickets/', views.view_booked_tickets, name='view_booked_tickets'),
    path('available-routes/', views.available_routes, name='available_routes'),
]