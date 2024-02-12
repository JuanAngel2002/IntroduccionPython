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
    
    if opcion==1:
        lista1 = ingresarLista()
    elif opcion==2:
        lista1.sort()
    elif opcion==3:
        lista1 = buscarLista(lista1)
    elif opcion==5:
        mostrarLista(lista1)
    elif opcion==7:
        lista1 = ingresarRandom()
    else:
        print("opcion no valida")


