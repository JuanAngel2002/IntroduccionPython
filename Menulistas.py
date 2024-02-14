import random
def ingresarLista():
    lista=[]
    dato=int(input("ingrese el número de datos a la lista: "))
    for i in range(dato):
        lista.append(int(input("ingrese un número: ")))  
    return lista

# def mostrarLista(lista):
#     for x in lista:
#         print(x)
def mostrarLista(lista):
    print("\n", lista)
    
def buscarLista(lista1):
    numero = int(input("ingrese el número a buscar: "))
    for i in lista1:
        if i == numero:
            print("el número",numero,"está en la posición",lista1.index(numero))
            return True
    print("el número",numero,"no está en la lista")
    
def ingresarRandom():
    lista=[]
    for i in range(20):
        lista.append(random.randint(1,100))
    return lista

def removerDato(lista1):
    dato = int(input("Ingrese el número a remover: "))
    if dato in lista1:
        lista1.remove(dato)
        print("El dato", dato, "se removió correctamente")
    else:
        print("El dato no se encuentra en la lista")
    return lista1

def updateDato():
    dato=int(input("ingrese el número a actualizar:"))
    if dato in lista1:
        dato1=int(input("ingrese el nuevo dato: "))
        indice = lista1.index(dato)
        lista1[indice]=dato1
        print("el dato se actualizó correctamente")
    else:
        print("el dato no se encuentra en la lista")
    
    
    
lista1 = []
opcion=1
while opcion!=0:
    print("""menú de manejo de listas: 
        1. Ingresar los datos de la lista
        2. Ordenar los datos de la lista
        3. Buscar un dato dentro de la lista
        4. Remover datos de una lista
        5. Mostrar la lista
        6. Actualizar un dato de la lista
        7. Agregar datos
        0. Salir
        """)
    opcion=int(input("Digite la opcion que desea: "))   
    if opcion==0:
        print("Saliendo...")
        break
    elif opcion==1:
        lista1 = ingresarLista()
    elif opcion==2:
        lista1.sort()
    elif opcion==3:
        lista1 = buscarLista(lista1)
    elif opcion==4:
        lista1 = removerDato(lista1)
    elif opcion==5:
        mostrarLista(lista1)
    elif opcion==6:
        updateDato()
    elif opcion==7:
        lista1 = ingresarRandom()
    else:
        print("opcion no valida")
        


