numeros = [int(x) for x in input("Digite a lista de números separados por espaço: ").split()]
numeros_pares = [x for x in numeros if x % 2 == 0]

if numeros_pares:
    media = sum(numeros_pares) / len(numeros_pares)
    print("Média dos números pares:", media)
else:
    print("Não há números pares na lista.")
