from django.db import models
from django import forms
from django.contrib.auth.models import User

# Updated to reflect cities and provinces in Ireland
CITIES_GROUPS = [
    ('Dublin', 'Cork', 'Galway', 'Limerick'),
    ('Waterford', 'Kilkenny', 'Wexford'),
    ('Donegal', 'Derry', 'Sligo'),
    ('Kerry', 'Clare', 'Tipperary'),
]
CITIES = [(city, city) for group in CITIES_GROUPS for city in group]

# Payment amounts might need adjustment for Euros
PAYMENT = [
    (15, 17),  # Example payment amounts in Euros
]
PAY = [(pay, pay) for group in PAYMENT for pay in group]

METHODS = [
    ('VISA', 'MASTERCARD', 'REVOLUT', 'BANK TRANSFER'),
]
WAY = [(method, method) for group in METHODS for method in group]


class Bus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    no_plate = models.CharField(max_length=150)
    seats = models.IntegerField()
    departure_city = models.CharField(max_length=150, choices=CITIES)
    arrival_city = models.CharField(max_length=100, null=True, choices=CITIES)
    departure_time = models.DateField() 
    depart_time = models.TimeField(null=True)
    is_available = models.BooleanField(default=False, null=True, verbose_name="is_available")

    def __str__(self):
        return f" \t{self.name } \t{self.no_plate} \t{self.seats} from \t{self.departure_city} at \t{self.departure_time} to \t{self.arrival_city}"


class Route(models.Model):
    id = models.BigAutoField(primary_key=True)
    departure_city = models.CharField(max_length=150, choices=CITIES)
    arrival_city = models.CharField(max_length=100, null=True, choices=CITIES)
    distance = models.FloatField()  
    timeTaken = models.DurationField() 
    buses = models.ManyToManyField(Bus, related_name='routes')

    def __str__(self):
        return f"\t from {self.departure_city}  \t{self.distance}km to  \t{self.arrival_city}"



#schedule model 
class Schedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departTime=models.DateTimeField()
    arrivalTime = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    route = models.ForeignKey(Route, on_delete= models.CASCADE)
    def __str__(self):
        return f"price is \t{self.price} departs at \t{self.departTime} "

#Ticket model 
class Ticket(models.Model):
    id = models.BigAutoField(primary_key=True)
    schedule=models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seat_no = models.CharField(max_length=50)
    passenger_name =models.CharField(max_length=100)
    passengerAge= models.IntegerField()
    gender=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    pay = models.IntegerField(null=True, choices=PAY)
    bus=models.ForeignKey(Bus, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.passenger_name} {self.schedule} {self.seat_no} {self.gender} {self.user}{self.pay}"
    
        

#payment model   
class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    paymentMethod = models.CharField(max_length=100, choices=WAY)
    transactionId= models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8, decimal_places=2)
    

#user profile
class UserProfile(models.Model):
    id = models.BigAutoField(primary_key=True)   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length= 15)
    booking_history = models.ManyToManyField(Ticket, blank=True)
    firstname = models.CharField(max_length= 100)
    secondName = models.CharField(max_length=100)
    email= models.CharField(max_length=200)


class Testing(models.Model):
    id = models.BigAutoField(primary_key=True)
    departure_date = models.DateField()
    No_of_seats = models.IntegerField()
    license = models.CharField(max_length=100)
    name = models.CharField(max_length= 100)
    



class Seat(models.Model):
    seat_number = models.IntegerField(unique=True)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f'Seat {self.seat_number}'
