from django.shortcuts import render
from mysite.models import Paquete, Vuelo, Hotel

def verPaquetes(request):
    paquetes = Paquete.objects.all()
    return render(request,"miarchivo.html",context={"paquetes" : paquetes})

def verVuelo(request):
    vuelos = Vuelo.objects.all()
    return render(request,"vuelo.html",context={"vuelos" : vuelos})

def verHotel(request):
    hotels = Hotel.objects.all()
    return render(request,"hotel.html",context={"hotels" : hotels})