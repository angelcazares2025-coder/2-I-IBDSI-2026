'''
2 I
Andre Luciano De la Torre Gutierrez
26/02/26
'''

print("BIENVENIDO")
nombre=input("cual es tu nombre?: ")
vigencia=input("cuanto años deseas que sea valido tu pasaporte?\n1-1año\n 2-3años\n3-6años\n4-10años\n")
destino=input("A que lugar quieres ir?\n1-usa\n2-europa\n3-japon\n4-corea del norte\n5-canada\n")

pasaporte={'1':920,'2':1790,'3':14440,'4':4280}

costo=0
match destino:
    case '1': costo=185
    case '5': costo=100+85+7
    case _: costo=0

dolar=float(input("cual es el valor del dolar hoy?: "))
total=pasaporte.get(vigencia)+costo*dolar
print(f'{nombre} necesitas ${total} para tener tu visa y pasporte')