#Metodo que agregara un numero mas
def numeroExtra():
    print('Multiplos de ...')
    print('Elije un rango de numeros: ')
    rangI = int(input('Numero Inicial: '))
    rangF = int(input('Numero Final: '))
    print('Elige ')
    print()
    print('Ahora elije tus numeros: ')
    num1 = int(input('Numero a convertir en Fizz: '))
    num2 = int(input('Numero a convertir en Buzz: '))
    numExt = int(input('Numero a convertir en Buzz: '))
    print(f'El rango de numeros del {rangI} al {rangF}: ')
    for n in range(rangI, rangF+1):
        if n%num1 == 0 and n%num2 == 0 and n%numExt == 0:
            print('Fizz Buzz Trizz')
        elif n%num1 == 0:
            print('Fizz')
        elif n%num2 == 0:
            print('Buzz')
        elif n%numExt == 0:
            print('Trizz')
        else:
            print(f'Numero: {n}')

    

#La raiz del programa sin metodos, llamara al metodo de arriba que tiene la opcion de agregar un tercer numero

print('Multiplos de ...')
print('Elije un rango de numeros: ')
rangI = int(input('Numero Inicial: '))
rangF = int(input('Numero Final: '))
print('Elige ')
print()
print('Ahora elije tus numeros: ')
num1 = int(input('Numero a convertir en Fizz: '))
num2 = int(input('Numero a convertir en Buzz: '))

print(f'El rango de numeros del {rangI} al {rangF}: ')
for n in range(rangI, rangF+1):
    if n%num1 == 0 and n%num2 == 0:
        print('Fizz Buzz')
    elif n%num1 == 0:
        print('Fizz')
    elif n%num2 == 0:
        print('Buzz')
    else:
        print(f'Numero: {n}')

print('Desea agregar un numero extra? S/N')
while True:
    try:
        respuesta = input('S/N: ') 
        if respuesta == 'S':
            numeroExtra()
            break
        if respuesta == 'N':
            print('Fin del programa')
            break
    except ValueError:
        print('Escriba la respuesta correcta')
