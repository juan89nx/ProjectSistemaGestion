from django.db import models

# Create your models here.
class Client(models.Model):
    nombre = models.CharField(max_length =250)
    apellido = models.CharField(max_length =250)
    cedula = models.CharField(max_length =10)
    fecha_de_nacimiento = models.DateField()
    telefono = models.CharField(max_length =250)
    celular = models.CharField(max_length =15)
    direccion = models.CharField(max_length =250)
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    fecha_creacion = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido
        #return models.Model.__str__(self)

class Vehicle(models.Model):
    Client = models.ForeignKey(Client, on_delete = models.CASCADE)
    tipo = models.CharField(max_length =250)
    matricula = models.CharField(max_length =10)
    marca = models.CharField(max_length =250)
    modelo = models.CharField(max_length =250)
    fecha_fabricacion = models.DateField()
    kilometraje =models.IntegerField(max_length =100)
    aclaraciones = models.CharField(max_length =250)

    def __str__(self):
        return self.Client.nombre + ' ' + self.Client.apellido+ ', ' + self.matricula
    
class Task(models.Model):
    Vehicle = models.ForeignKey(Vehicle, on_delete = models.CASCADE)
    nombre = models.CharField(max_length =250)
    descripcion = models.CharField(max_length =250)
    icono = models.CharField(max_length =1000)
    estado = models.CharField(max_length =50)
    fecha_creacion = models.DateTimeField()
    fecha_comienzo = models.DateTimeField()
    fecha_finalizacion = models.DateTimeField()
    responsable = models.CharField(max_length =250)
    
    def __str__(self):
        return self.Vehicle.matricula + ', ' + self.nombre
    