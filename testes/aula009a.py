frase = 'Curso em Vídeo Python'
print(frase)

print("-" * 15)
print("Fatiamento")
print("-" * 15)
print(frase[9])  # Imprime o caractere da posição 9
print(frase[9:13])  # Imprime da posição 9 até a 12
print(frase[9:14])  # Imprime da posição 9 até a 13
print(frase[9:21])  # Imprime da posição 9 até a 20
print(frase[9:21:2])    # Imprime da posição 9 até a 20 pulando 2 posições
print(frase[:5])    # Imprime do início até a posição 4
print(frase[15:])   # Imprime da posição 15 até o final
print(frase[9::3])  # Imprime da posição 15 até o final pulando 3 posições
print(frase[::3])   # Imprime da posição inicial até a final pulando 3 posições

print("\n" + "-" * 15)
print("Análise")
print("-" * 15)
print("Comprimento da String: {}".format(len(frase)))
print("Quantidade do caractere 'o': {}".format(frase.count('o')))
print("Quantidade do caractere 'O': {}".format(frase.count('O')))
print("Quantidade do caractere 'o' em um pedaço da string: {}".format(frase.count('o', 0,13)))
print("Em qual posição o 'deo' está na String? {}".format(frase.find('deo')))
print("Em qual posição o 'Android' está na String? {}".format(frase.find('Android')))
print("Existe a palavra 'Curso' na String? {}".format("Curso" in frase))

print("\n" + "-" * 15)
print("Transformação")
print("-" * 15)
print(frase.replace("Python","Android"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = '   Aprenda Python  '
print(frase)
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

print("\n" + "-" * 15)
print("Divisão")
print("-" * 15)
frase = 'Curso em Vídeo Python'
print(frase)
separar = frase.split()
print(separar)
print("-".join(frase))
print("-".join(separar))

print("\n" + "-" * 15)
print("Imprimir texto longo")
print("-" * 15)
print("""Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String, 
Análise com len(), count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(), strip(), junção com join().""")