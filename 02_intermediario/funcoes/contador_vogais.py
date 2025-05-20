# Crie uma função que retorna quantas vogais existem em uma string.


VOGAIS = 'aeiouéíóúõã'

def contar_vogais(palavra):
    cont = 0
    for letra in palavra:
        if(letra in VOGAIS):
            cont+=1
    return cont


palavra = input("Informe uma palavra: ")

if(not palavra.isalpha() or len(palavra) < 2):
    print("Informe uma palavra válida!")

else:
    print(f"A palavra {palavra} tem {contar_vogais(palavra)} vogal(is)")


