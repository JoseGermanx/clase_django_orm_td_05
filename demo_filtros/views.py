from django.http import HttpResponse

from django.db.models import Q, F
from .models import Cliente

# Create your views here.

def demo_filtros(request):

    print("Demo 1  -- --- F()")
    # Clientes donde las visitas > pedidos
    clientes_filtrados = Cliente.objects.filter(visitas__gt=F('pedidos'))
   
    for cliente in clientes_filtrados:
        print(cliente.nombre, cliente.visitas, cliente.pedidos)

    print("Demo 2  -- --- Q()")
    # Clientes activos y mayores a 25
    clientes_activos_mayores_25 = Cliente.objects.filter(Q(activo= True) & Q(edad__gte=25))
    
    for cliente in clientes_activos_mayores_25:
        print(cliente.nombre, cliente.edad, cliente.activo)

    print("Demo 3  -- ---  Q()")
    #Clientes activos o vivan en Rancagua

    cliente_activos_o_rancagua = Cliente.objects.filter(Q(activo=False) | Q(ciudad="Rancagua"))
    for cliente in cliente_activos_o_rancagua:
        print(cliente.nombre, cliente.ciudad, cliente.activo)

    
    print("Demo 4  -- ---  ~Q()")
    # Clientes no activos
    cliente_no_activos= Cliente.objects.filter(~Q(activo=False))
    for cliente in cliente_no_activos:
        print(cliente.nombre, cliente.ciudad, cliente.activo)




    return HttpResponse("Revisa la terminal de Django!!")