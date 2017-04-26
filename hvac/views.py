from django.shortcuts import render

def start_page(request):
    return render(request, 'start.html')

def new_thermostat(request):
    return render(request, 'new.html')
