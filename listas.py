listas = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
#si quiero mostrar hasta cierto punto los datos de la lista, con los dos puntos ponemos hasta el 
#rango que va llegar pero restandole uno, osea si ponemos hasta 3 va a mostrar hasta la possición 2
#si no ponemos nada despues de los dos puntos, python sabe que es hasta el final
print(listas[0:3])
#la funcion len es para que el programa nos diga cuantos elementos tiene la lista
print(len(listas))

#funcion para agregar elementos al final de la lista
#lista.append(6)

#funcion para agregar elementos donde nostros queremos
#lista.insert(2,"Lunes")

#para agregar varios elementos de una vez
#lista.extend(["Lunes","Martes","Miercoles","Jueves","Viernes"])

#para buscar elementos
#print(valorquequiero in nombre de la lista)

#para buscar el indice de algun elemento
#print(listas.index(valor que deseas buscar))

#para mostrar cuantos valores repetidos hay
#print(lista.count(valor que deseas))

#para eliminar, si no se pone nada elimina el último elemento, ya si quiero uno en específico dentro de los 
#parentesis el indice que desea eliminar
#lista.pop()

#otro metdodo para eliminar pero este elimina el valor que se ponga
#lista.remove(valor que deseas eliminar)
