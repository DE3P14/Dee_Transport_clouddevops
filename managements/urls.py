from django.urls import path, include
from . import views
from .views import logout_view
from .views import view_all_buses



urlpatterns = [ 
               
    path('',views.home, name="homepage"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', views.homepage, name='home'),
    path('search_routes/', views.search_routes, name='search_routes'),
    path('search_form/', views.search_form, name='search_form'),
    path('booking/', views.booking, name='booking'),
    path('ticket/<int:ticket_id>/', views.print_ticket, name='print_ticket'),
    path('print-ticket/', views.print_ticket, name='print_ticket'),
    path('save_ticket/', views.save_ticket, name='save_ticket'),
    path('book-ticket/<int:schedule_id>/', views.book_ticket, name='book_ticket'),
    path('ticket_confirmation/', views.ticket_confirmation, name='ticket_confirmation'),
    path('all_buses/', view_all_buses, name='all_buses'),
    path('create_bus/', views.create_bus, name='create_bus'),
    path('update_bus/<int:pk>/', views.update_bus, name='update_bus'),
    path('delete_bus/<int:pk>/', views.delete_bus, name='delete_bus'),
    path('buses/create/', views.create_bus, name='create_bus'),
    path('bus/<int:pk>/', views.bus_detail, name='bus_detail'),

]
