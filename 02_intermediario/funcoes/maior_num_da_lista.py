# Maior Número de uma Lista

#Crie uma função que retorna o maior número de uma lista.

def maior_num(*numero):
    for num in numero:
        maior = numero[0]
        if(maior < num):
            maior = num
    print(f"Maior número da lista: {maior}")

maior_num(1,5,8,9,50)