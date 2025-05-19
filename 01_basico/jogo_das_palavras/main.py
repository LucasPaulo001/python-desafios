#O usuário terá que adivinhar a palavra escondida
import random

palavras = [ "carro", "casa", "bicicleta", "bola", "cachorro", "peixe" ]

palavra_correta = random.choice(palavras)

print("\n----Acerte a palavra escondida----\n")

mascara_palavra = ""
for letra in palavra_correta:
    mascara_palavra += "*"

print(mascara_palavra)

letra_correta = set()
tentativas = 0

while True:
    
    resp_usuario = input("\nInforme uma letra: ")
    tentativas += 1
    
    #Validações
    if(not resp_usuario.isalpha() or not resp_usuario):
        print("Informe uma letra válida!")

    if(len(resp_usuario) > 1):
        print("Informe apenas uma letra!")
        continue
    
    
    if(resp_usuario in palavra_correta):
        letra_correta.add(resp_usuario)

        if(letra_correta >= set(palavra_correta)):
            print(f"PARABÉNS! você acertou a palavra => '{palavra_correta}' ")
            print(f"Tentativas: {tentativas}")
            break

    palavra_formada = ""
    for letra in palavra_correta:
        if (letra in letra_correta):
            palavra_formada += letra
    
        else:
            palavra_formada += "*"

    print(palavra_formada)
    


