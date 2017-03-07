from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
                       
    # Examples:
    # url(r'^$', 'ProjectSistemaGestion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='Home'),
    url(r'^home', views.home, name='Home'),
    
    #GestionArt/client/newClient
    url(r'^client/newClient', views.newClient, name = 'New Client'),
     
    #GestionArt/client/[clientID] 
    url(r'^client/(?P<client_id>[0-9]+)$', views.client, name = 'Client'),
    
    #GestionArt/client/clientList
    url(r'^client/clientList', views.clientList, name = 'Client List'),
    
    #GestionArt/vehicle/newVehicle
    url(r'^vehicle/newVehicle', views.newVehicle, name = 'New Vehicle'),
    
    #GestionArt/vehicle/[vehicleID] 
    url(r'^vehicle/(?P<client_id>[0-9]+)$', views.vehicle, name = 'Vehicle'),
    
    #GestionArt/client/vehicleList
    url(r'^vehicle/vehicleList', views.vehicleList, name = 'Vehicle List'),

    #GestionArt/task/newTask
    url(r'^task/newTask', views.newTask, name='New Task'),

    #GestionArt/task/[TaskID]  >  task/712/
    url(r'^task/(?P<task_id>[0-9]+)$', views.task, name='Task'),

    #GestionArt/task/taskList
    url(r'^task/taskList', views.taskList, name = 'Task List'),
    
    
    url(r'^allTaskDetails', views.allTasksDetails, name = 'allTaskDetails'),
    url(r'^allTareasViejo', views.allTareasViejo, name = 'allTareasViejo'),

)



