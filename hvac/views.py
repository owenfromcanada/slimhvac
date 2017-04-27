from django.shortcuts import redirect, render

from hvac.models import Thermostat

def start_page(request):
    if request.method == 'POST':
        Thermostat.objects.create(name=request.POST['name_text'], zwave_id=request.POST['zwave_id_text'])
        return redirect('/')
    return render(request, 'start.html')

def new_thermostat(request):
    return render(request, 'new.html')
