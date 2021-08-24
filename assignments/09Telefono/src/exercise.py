def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
a = int(input("Dame el numero de mensajes:"))
b = float(input("Dame el numero de megas:"))
c = int(input("Dame el numero de minutos:"))
d = a*.8
e = b*.8
f = c*.8
cm = d+e+f
print("el costo mensual es:")
print(cm)


if __name__ == '__main__':
    main()
