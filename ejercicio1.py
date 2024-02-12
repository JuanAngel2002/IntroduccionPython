hectareas=int(input("Digite el tamaño de su terreno: "))

metroscua=hectareas*10000

if metroscua>1000000 :
    pinos=((metroscua*0.7)/10)*8
    oyamel=((metroscua*0.2)/15)*15
    cedro=((metroscua*0.1)/18)*10
else:
    pinos=((metroscua*0.5)/10)*8
    oyamel=((metroscua*0.3)/15)*15
    cedro=((metroscua*0.2)/18)*10
    
print("el numero de pinos es: ",pinos,"\nel numero de oyamel es: ",oyamel,"\nel numero de cedro es: ",cedro)
    