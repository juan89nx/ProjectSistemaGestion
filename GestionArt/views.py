from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request
from django.template import loader
from .models import Client, Vehicle, Task

def home(request):
    return render(request, 'pages/home.html', {})

def newClient (request):
    return render(request, 'pages/newClient.html', {})

def client (request, client_id):
    myClient = Client.objects.get(id=client_id)
    context = {
        'myClient': myClient,
    } 
    return render(request, 'pages/client.html', context)

def clientList (request):
    all_clients = Client.objects.all()
    context = {
        'all_clients': all_clients,
    } 
    return render(request, 'pages/clientList.html', context)


def newVehicle (request):
    return render(request, 'pages/newVehicle.html', {})

def vehicle (request, vehicle_id):
    myVehicle = Vehicle.objects.get(id=vehicle_id)
    print(myVehicle)
    context = {
        'myVehicle': myVehicle,
    } 
    return render(request, 'pages/vehicle.html', context)

def vehicleList (request):
    all_vehicles = Vehicle.objects.all()
    context = {
        'all_vehicles': all_vehicles,
    } 
    return render(request, 'pages/vehicleList.html', context)



def newTask (request):
    return render(request, 'pages/newTask.html', {})

def task (request, task_id):
    myTask = Task.objects.get(id=task_id)
    context = {
        'myTask': myTask,
    } 
    return render(request, 'pages/task.html', context)

def taskList(request):
    all_tasks = Task.objects.all()
    context = {
        'all_tasks': all_tasks,
    }    
    return render(request, 'pages/taskList.html', context)


#OLD For Testing
def allTasksDetails(request):
    all_tasks = Task.objects.all()
    context = {
        'all_tasks': all_tasks,
    }    
    return render(request, 'pages/allTasksDetails.html', context)

def allTareasViejo(request):
    return render(request, 'pages/allTareasViejo.html', {})
   
def index(request):
    return render(request, 'pages/homeViejo.html', {})

