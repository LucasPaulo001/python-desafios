#Entrada de dois números e uma operação: soma, subtração, multiplicação ou divisão.

print("\nCalculadora simples\n")

num01 = input("Informe o primeiro número: ")
num02 = input("Informe o segundo número: ")

if(not num01.isdigit() or not num02.isdigit()):
    print("Informe um valor válido para o cálculo!")

else:

    #Validações

    operador = input("Informe o operador [+-*/]: ")
    operadores = "+-/*"

    #Validações

    if(len(operador) > 1):
        print("Escolha apenas um dos operadores!")

    if(operador not in operadores):
        print("Informe um operador válido! ")

    #Cálculos

    num01_int = int(num01)
    num02_int = int(num02)

    if(operador == '+'):
        soma = num01_int + num02_int
        print(f"\nResultado: {soma}")

    if(operador == '-'):
        sub = num01_int - num02_int
        print(f"\nResultado: {sub}")

    if(operador == '*'):
        mult = num01_int * num02_int
        print(f"\nResultado: {mult}")
    if(operador == '/'):
        if(num02_int == 0):
            print("\nNão existe divisão por zero!")
        else:
            div = num01_int // num02_int
            print(f"\nResultado: {div}")



