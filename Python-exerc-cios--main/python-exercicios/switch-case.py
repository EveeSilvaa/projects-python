"""
EXERCÍCIO: implemente o exemplo de switch case acima usando as condições "if/else"

Prompt: para cada dígito entre 0-9, o programa imprimirá uma confirmação 
para o valor inserido ou irá imprimir "invalid inputs" para todos os outros números.
"""

print("Escolha um número inteiro de 0 a 9.")
numero = input()

def switcher(numero):
    numero = int(numero)
    if 0 <= numero <= 9:
        print("O número escolhido foi: ", numero)
    else:
        print("O número escolhido é inválido, se atente às condições.")

switcher(numero)