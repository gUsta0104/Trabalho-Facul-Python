arquivo = open("loremimpsum.txt", "r", encoding="utf-8")

conteudo = arquivo.read()

print(conteudo)

arquivo.close()

with open("loremimpsum.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readline()
    print(linhas)

with open("loremimpsum.txt", "r", encoding="utf-8") as arquivo:
    letras = arquivo.read(3)
    print(letras)