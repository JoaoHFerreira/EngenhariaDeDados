# Tipagem dinâmica, significa que inteiros podem virar strings ou vice versa .
# Script, quer dizer que não compilada pra código de máquina como por exemplo C, golang
# Orientado a objetos, estruturado, com uma pegada funcional.

valor = 3


if valor > 2:
    print("O valor é maior que 2")
    if valor == 3:
        print("agora é igual a 3")
    #Elif está relacionado com o if
    # Podem ter N elifs
    # Os níveis de identação definem o relacionamento condicional
    elif valor < 2:
        print("O valor é menor que 2")
    else:
        print("Nada deu certo...")

# Estruturas de loop
# for e o while

# Snake case quando palavras separadas por underline
lista_de_valores = [1,2,3,4,5,6,"uma string", 7, "outra string"]

print(lista_de_valores)
print(lista_de_valores[0])
print(lista_de_valores[1])
print(lista_de_valores[2])


# Printa valores da lista iniciando pelo índice zero 
for valor in lista_de_valores:
    print(valor)

# While define uma condição para realizar a sua repetição
index = 0 
while index < 5:
    print(lista_de_valores[index])
    index += 1
