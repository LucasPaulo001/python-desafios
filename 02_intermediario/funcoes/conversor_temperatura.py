# Conversor de Temperatura com Closure

'''

Crie uma função criar_conversor que recebe uma unidade de temperatura de destino ("C" ou "F").

Ela deve retornar uma função que recebe uma temperatura e converte para a unidade desejada.

°F = (9/5) * °C + 32

°C = (5/9) * (°F - 32)

'''

UNIDADE = "cf"

def criar_conversor(temp_destino):
    def conversror(temperatura):

        if(temp_destino == "c"):
            return f"Valor em ºC: {((5/9) * (temperatura - 32)):.2f}"
        
        return f"Valor em ºF: {((9/5) * temperatura + 32):.2f}"
    
    return conversror

temperatura = input("Informe a temperatura em ºC ou ºF: ")

if(not temperatura.isdigit()):
    print("Informe uma temperatura válida!")

else:
    unidade = input("Informe o a unidade de medida que você quer converter [para ºC = [c] para ºF = [f]]: ").lower()

    if unidade not in UNIDADE:
        print("Informe uma unidade válida! [°C ou ºF]!")

    else:

        conversor_para_celsius = criar_conversor(unidade)

        print(conversor_para_celsius(float(temperatura)))
