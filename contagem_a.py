def contar_a(texto):
    # Converte a string para minúsculas e conta todas as ocorrências de 'a'
    contagem = texto.lower().count('a')
    
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Solicita a entrada de uma string do usuário
entrada = input("Digite uma string: ")

# Chama a função para contar e verificar a presença da letra 'a'
contar_a(entrada)