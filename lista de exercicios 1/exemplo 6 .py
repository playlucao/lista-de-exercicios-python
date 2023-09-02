def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

num = int(input("Digite um número inteiro positivo: "))

if num < 0:
    print("Número deve ser positivo.")
else:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é {resultado}")
