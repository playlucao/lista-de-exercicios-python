def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Digite um número: "))

if eh_primo(num):
    print("É um número primo.")
else:
    print("Não é um número primo.")
