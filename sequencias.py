# Sequência a: 1, 3, 5, 7, ___
def sequencia_a():
    numeros = [1, 3, 5, 7]
    proximo_numero = numeros[-1] + 2  # Lógica: somar 2 ao último número
    return proximo_numero

# Sequência b: 2, 4, 8, 16, 32, 64, ____
def sequencia_b():
    numeros = [2, 4, 8, 16, 32, 64]
    proximo_numero = numeros[-1] * 2  # Lógica: multiplicar o último número por 2
    return proximo_numero

# Sequência c: 0, 1, 4, 9, 16, 25, 36, ____
def sequencia_c():
    numeros = [0, 1, 4, 9, 16, 25, 36]
    proximo_numero = (len(numeros)) ** 2  # Lógica: quadrados perfeitos
    return proximo_numero

# Sequência d: 4, 16, 36, 64, ____
def sequencia_d():
    numeros = [4, 16, 36, 64]
    proximo_numero = (len(numeros) * 2) ** 2  # Lógica: quadrados de números pares
    return proximo_numero

# Sequência e: 1, 1, 2, 3, 5, 8, ____
def sequencia_e():
    numeros = [1, 1, 2, 3, 5, 8]
    proximo_numero = numeros[-1] + numeros[-2]  # Lógica: sequência de Fibonacci
    return proximo_numero

# Sequência f: 2, 10, 12, 16, 17, 18, 19, ____
def sequencia_f():
    numeros = [2, 10, 12, 16, 17, 18, 19]
    proximo_numero = numeros[-1] + 1  # Lógica: números consecutivos após múltiplos de 2
    return proximo_numero

# Exibir os próximos números de cada sequência
print("Sequência a: Próximo número é", sequencia_a())
print("Sequência b: Próximo número é", sequencia_b())
print("Sequência c: Próximo número é", sequencia_c())
print("Sequência d: Próximo número é", sequencia_d())
print("Sequência e: Próximo número é", sequencia_e())
print("Sequência f: Próximo número é", sequencia_f())
