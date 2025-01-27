import string

def palindromoOuNao(frase):
    exclude = set(string.punctuation)
    frase = ''.join(ch for ch in frase if ch not in exclude)
    frase = frase.replace(" ", "").lower()
    frase = str(frase)
    if frase == frase[::-1]:
        return frase + " é um palíndromo (> . <)"
    else:
        return frase + " não é um palíndromo (> ~ <)"

def main():
    print("Escreva uma frase ou palavra para saber se ela é um palíndromo ou não.")
    escolhaDoUsario = input()
    print(palindromoOuNao(escolhaDoUsario))

if __name__ == "__main__":
    main()