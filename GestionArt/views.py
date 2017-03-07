from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request
from django.template import loader
from .models import Client, Vehicle, Task


# Create your views here.
#PRUEBA JUAN_____________________________________MAGIC
def clientList(request):
    all_clients = Client.objects.all()
    all_vehicules = Vehicle.objects.all()
    html=''
    for client in all_clients:
        for vehicle in all_vehicules:
            url = '/gestionArt/client/'+str(client.id)
            html += '<a href="'+url+'">'+ vehicle.Client.nombre+'</a><br>'
    return HttpResponse(html)

def home(request):
    return render(request, 'pages/home.html', {})

def allTasksDetails(request):
    all_tasks = Task.objects.all()
    #template = loader.get_template('templates/pages/allTasksDetails.html')
    context = {
        'all_tasks': all_tasks,
    }    
    return render(request, 'pages/allTasksDetails.html', context)

def allTareasViejo(request):
  return render(request, 'pages/allTareasViejo.html', {})
   

def task(request, task_id):
    #return render(request, 'pages/newTask.html', {})
    return HttpResponse("<h1>Details for Task id: </h1>"+str(task_id))

def newClient (request):
    return render(request, 'pages/newClient.html', {})

def client (request, client_id):
    myClient = Client.objects.get(id=client_id)
    context = {
        'myClient': myClient,
    } 
    return render(request, 'pages/client.html', context)

def newVehicle(request):
    return render(request, 'pages/newVehicle.html', {})

def vehicleList(request):
    return render(request, 'pages/vehicleList.html', {})
