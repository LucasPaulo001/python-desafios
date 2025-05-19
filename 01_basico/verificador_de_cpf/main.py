#Validar a estrutura e calcular os dígitos verificadores.

#Exemplo: 74682489070
#(9 primeiros dígitos: 746824890, últimos 2: dígitos verificadores)

print("\nVerificador de CPF\n")

cpf = '74682487070'

mult = 10
soma = 0

#Verificação do primeiro dígito

for digit in cpf[:9]:
    res_mult = int(digit) * mult
    mult -= 1
    soma += res_mult

digito01 = (soma * 10) % 11

digito01 = 0 if digito01 > 9 else digito01

#Verificação do segundo dígito

mult_digito02 = 11
soma_digito02 = 0
for digit in cpf[:10]:
    res_mult02 = int(digit) * mult_digito02
    mult_digito02 -= 1
    soma_digito02 += res_mult02
    

digito02 = (soma_digito02 * 10) % 11

digito02 = 0 if digito02 > 9 else digito02

#Pegando os dois últimos dígitos do cpf
digito01_cpf = cpf[9]
digito02_cpf = cpf[10]

if(digito01 == int(digito01_cpf) and digito02 == int(digito02_cpf)):
    print("O CPF é válido!!")

else:
    print("O CPF não é válido!!")

    