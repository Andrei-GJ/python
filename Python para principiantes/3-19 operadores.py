a=int(input("di un numero"))
print("el numero escogido es:",a)

b=int(input("di otro numero"))
print("el numero escogido es:",b)

print("la suma de 'a' y de 'b' es",a + b)
print("la resta de 'a' y de 'b' es:",a - b)
print("la multiplicacion de 'a' y de 'b'es:",a * b)
print("la divicion de 'a' y de 'b' es:",a / b)
print("la potencia de 'a' y de 'b' es:",a ^ b)
print("la divicion entera de 'a' y de 'b'es:",a % b)

print(a ,"sumado con",b,"es igual a",a + b)
print(a ,"restado con",b,"es igual a",a - b)
print(a ,"multiplicado con",b,"es igual a",a * b)
print(a ,"dividido con",b,"es igual a",a / b)
print(a ,"potenciado con",b,"es igual a",a ^ b)
print(a ,"dividido exactamente con",b,"es igual a",a % b)

#operadores logicos 

#basicamente son 3 and or not (AND) si ambos dan igual da true si uno es diferente da false (OR) si aunque sea uno es correcto da true (NOT) al parecer es la contra de AND

x=7
y=15
print(x < 5 and y < 10)

print(not(x < 5  and y <10))
