def is_fibonacci(n):
    # Iniciando a sequência de Fibonacci
    fib1, fib2 = 0, 1
    # Se o número informado for 0 ou 1, já é parte da sequência
    if n == 0 or n == 1:
        return True
    
    # Calcula a sequência de Fibonacci até que fib2 seja maior ou igual a n
    while fib2 < n:
        fib1, fib2 = fib2, fib1 + fib2
    
    # Verifica se o número faz parte da sequência
    return n == fib2

# Solicita a entrada do número ao usuário
numero = int(input("Informe um número: "))

# Chama a função para verificar se o número está na sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")