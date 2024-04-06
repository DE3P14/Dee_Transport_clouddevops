from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm,  SearchForm, BookingForm, TicketForm, PrintTicketForm
from django.contrib.auth.models import User
from .models import Route, Bus, UserProfile,  Schedule, Ticket
from .forms import BusForm
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bus
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Alias the imported login function
from .forms import LoginForm
from .models import PAY

def homepage(request):
    return render(request, 'h.html')


def home(request):
    return render(request, 'home.html')



#fetch all buses without filters
def view_all_buses(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to prevent form resubmission
            return redirect('view_all_buses')
    else:
        form = BusForm()
    all_buses = Bus.objects.all()
    return render(request, 'all_buses.html', {'buses': all_buses, 'form': form})


def create_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_buses')
    else:
        form = BusForm()
    return render(request, 'create_bus.html', {'form': form})


def update_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
            return redirect('all_buses')
    else:
        form = BusForm(instance=bus)
    return render(request, 'update_bus.html', {'form': form})

def delete_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == "POST":
        bus.delete()
        return redirect('all_buses')
    return render(request, 'delete_bus_confirm.html', {'bus': bus})



@require_GET
def bus_detail(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    return render(request, 'bus_detail.html', {'bus': bus})



#register
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')    
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

 

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use the aliased auth_login here
                return redirect('home')  # Ensure this points to your homepage URL name
            else:
                # It's better to use a generic error message for security
                return render(request, 'login.html', {'form': form, 'error_message': 'Incorrect login credentials.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')




def login_view(request):  # Consider renaming to avoid confusion with `login` method
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Use 'user' instead of 'User'
            if user is not None:
                login(request, user)  # This line logs the user in
                return redirect('home')  # Ensure 'home' is the correct name of your homepage urlpattern
            else:
                # It's more secure not to tell whether the username or password was incorrect
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login credentials.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def search_routes(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            departure_city = form.cleaned_data['departure_city']
            arrival_city = form.cleaned_data['arrival_city']
            departure_time = form.cleaned_data['departure_time']
            matching_routes = Route.objects.filter(
                departure_time = departure_time,
                departure_city=departure_city,
                arrival_city=arrival_city
            )
            return render(request, 'route_list.html', {'routes': matching_routes})
    else:
        form = SearchForm()    
    return render(request, 'search.html', {'form': form})



#1 search
def search_form(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            departureTown = form.cleaned_data['departure_city']
            arrivalTown = form.cleaned_data['arrival_city']    
            departureTime = form.cleaned_data['departure_time']
            matching_buses = Bus.objects.filter(departure_city=departureTown, arrival_city=arrivalTown, departure_time=departureTime)
            return render(request, 'search_results.html', {'matching_buses': matching_buses})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})


@login_required
def booking(request, id):
    schedule = Schedule.objects.all()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.schedule = schedule  
            return redirect('booking_success') 
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form, 'schedule': schedule})







def print_ticket(request):
    if request.method == 'POST':
        form = PrintTicketForm(request.POST)
        if form.is_valid():
            ticket_id = form.cleaned_data['ticket_id']
            try:
                ticket = Ticket.objects.get(id=ticket_id)
                return render(request, 'print_ticket.html', {'ticket': ticket})
            except Ticket.DoesNotExist:
                return HttpResponse('Ticket not found')
    else:
        form = PrintTicketForm()
    return render(request, 'print_ticket_form.html', {'form': form})




def book_ticket(request, schedule_id):
    schedule = Schedule.objects.get(id=schedule_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            passenger_name = form.cleaned_data['passenger_name']
            passenger_age = form.cleaned_data['passenger_age']
            gender = form.cleaned_data['gender']
            payment_method = form.cleaned_data['payment_method']

            ticket = Ticket.objects.create(
                schedule=schedule,
                passenger_name=passenger_name,
                passengerAge=passenger_age,
                gender=gender,
                user=request.user,
                pay=payment_method
            )

            # Assuming payment processing here, create a payment object
            # payment = Payment.objects.create(ticket=ticket, ...)

            # Redirect to a page where the user can print their ticket
            return redirect('print_ticket', ticket_id=ticket.id)
    else:
        form = TicketForm()
    return render(request, 'book_ticket.html', {'form': form, 'schedule': schedule})







@login_required
def save_ticket(request):
    if request.method == 'POST':
        schedule_id = request.POST.get('schedule')
        schedule = get_object_or_404(Schedule, pk=schedule_id)
        
        bus_id = request.POST.get('bus')
        bus = get_object_or_404(Bus, id=bus_id)
        
        # Assuming the rest of the form data is valid and complete
        # Create the Ticket object here with the POST data received
        ticket = Ticket.objects.create(
            schedule=schedule,
            seat_no=request.POST.get('seat_no'),
            passenger_name=request.POST.get('passenger_name'),
            passengerAge=request.POST.get('passengerAge'),
            gender=request.POST.get('gender'),
            user=request.user,
            pay=request.POST.get('pay'),
            bus=bus
        )
        # Redirect to the ticket confirmation page after successful POST request handling
        return redirect('ticket_confirmation')
    else:
        # Define 'schedules' before using it to render the template for GET requests
        schedules = Schedule.objects.all()
        buses = Bus.objects.all()
        pays = PAY  # Ensure this is defined and accessible as well
        
        # Use the defined 'schedules' (and other context variables) here
        return render(request, 'ticket_form.html', {'schedules': schedules, 'buses': buses, 'pays': pays})



def ticket_confirmation(request):
    # Fetch the last ticket added to the database
    last_ticket = Ticket.objects.order_by('-id').first()
    if last_ticket:
        return render(request, 'ticket_confirmation.html', {'ticket': last_ticket})
    else:
        # Handle case where there are no tickets in the database
        return render(request, 'ticket_confirmation.html', {'ticket': None})

