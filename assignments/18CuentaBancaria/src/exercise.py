def main():
    #escribe tu código abajo de esta linea
a = float(input("Dame el saldo del mes anterior:"))
b = float(input("Dame los ingresos:"))
c = float(input("Dame los egresos:"))
d = int(input("Dame el número de cheques:"))
e = d*13
f = a+b-c-e
g = f*.075
h = f-g
print("El saldo final de la cuenta es:")
print(h)

if __name__ == '__main__':
    main()
