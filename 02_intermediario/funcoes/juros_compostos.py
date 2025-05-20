#Desafio: Simulador de Juros Compostos com Closure
'''
Crie uma função chamada simulador_juros que:

Recebe a taxa de juros anual (em decimal, ex: 0.10 para 10%) e o número de anos.

Retorna uma função interna que:

Recebe o valor inicial investido.

Calcula e retorna o valor final após o período com juros compostos.

'''

def simulador_juros(juros_anuais, anos):
    def calc_juros(valor_inicial):
        return valor_inicial * pow((1 + juros_anuais), anos)
    return calc_juros


simulador_10_anos = simulador_juros(.8, 10)

print(f"Juros do valor: {simulador_10_anos(1000):.2f}")