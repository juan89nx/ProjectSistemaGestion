from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProjectSistemaGestion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='Home'),
    
    url(r'^allTasksDetails', views.allTasksDetails, name = 'Todas las Tareas'),
    
    url(r'^allTareasViejo', views.allTareasViejo, name = 'allTareasViejo'),
    
    
    #GestionArt/task/TaskID  >  task/712/
    url(r'^task/(?P<task_id>[0-9]+)$', views.task, name='Task Details'),
    
    #GestionArt/newClient
     url(r'^client/newClient', views.newClient, name = 'New Client'),
     
     #GestionArt/client/TaskID 
     url(r'^client/(?P<client_id>[0-9]+)$', views.client, name = 'Client'),
     
    #GestionArt/client/clientList
     url(r'^client/clientList', views.clientList, name = 'Client List'),
     
      #GestionArt/vehicle/newVehicle
     url(r'^vehicle/newVehicle', views.newVehicle, name = 'New Vehicle'),
     
      #GestionArt/client/vehicleList
     url(r'^vehicle/vehicleList', views.vehicleList, name = 'Vehicle List'),
)



