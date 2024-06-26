from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Ticket, CITIES_GROUPS, CITIES, Bus, WAY, METHODS
from django.forms.widgets import DateInput, TimeInput

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'firstname', 'secondName', 'email']
        

class PaymentForm(forms.Form):
    payment_method = forms.CharField(max_length=100)
    transaction_id = forms.CharField(max_length=100)
    amount = forms.DecimalField(max_digits=8, decimal_places=2)



class BookingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['schedule', 'seat_no', 'passenger_name', 'passengerAge', 'gender']


class SearchForm(forms.Form):
    departure_city=  forms.ChoiceField(choices=CITIES)
    arrival_city=  forms.ChoiceField(choices=CITIES)
    departure_time = forms.DateField(
        label='Departure Date',
        input_formats=["%Y-%m-%d", "%m/%d/%Y", "%m/%d/%y"],
        widget=forms.DateInput(attrs={'type': 'date'})
        )



class TicketForm(forms.Form):
    passenger_name = forms.CharField(max_length=100)
    passenger_age = forms.IntegerField()
    gender = forms.ChoiceField(choices=(('male', 'Male'), ('female', 'Female')))
    payment_method = forms.ChoiceField(choices=METHODS)


class PrintTicketForm(forms.Form):
    ticket_id = forms.IntegerField(label='Ticket ID')


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'
        widgets = {
            'departure_time': DateInput(attrs={'type': 'date'}),
            'depart_time': TimeInput(attrs={'type': 'time'}),
        }