palavras = list()

with open("texto2.txt", "r", encoding='utf-8') as arquivo:
    for linha in arquivo:
        partes = linha.split()
        palavras.extend(partes)

sort_lista = palavras.copy()

sort_lista.sort()
print(sort_lista)

with open("texto3.txt", "w", encoding='utf-8') as arquivo:
    for palavra in sort_lista:
        arquivo.write(palavra + "\n")