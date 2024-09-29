# Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.


# Variáveis de inicialização

Quantidade_numeros = 0
Soma_numeros = 0

# Loop para ler números inteiros até que o usuário digite 0 (zero)

while True:
    Numeros_inteiros = int(input("Digite um número inteiro (ou 0 para sair): "))
    
    if Numeros_inteiros == 0:
        break
    
    Quantidade_numeros += 1
    Soma_numeros += Numeros_inteiros

# Verifica se algum número foi digitado

if Quantidade_numeros > 0:
    Média_aritmetica = Soma_numeros / Quantidade_numeros
    
    # Exibe a quantidade de números digitados, a soma e a média aritmética
    
    print("Quantidade de números digitados: ", Quantidade_numeros)
    print("Soma dos números digitados: ", Soma_numeros)
    print("Média aritmética: {:.2f}".format(Média_aritmetica))

else:
    print("Nenhum número foi digitado.")


