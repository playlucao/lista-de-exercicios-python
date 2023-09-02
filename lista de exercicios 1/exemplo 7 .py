def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

limite = int(input("Digite um valor limite para a sequência de Fibonacci: "))
fibonacci(limite)
