# Define o número a ser verificado
num = 50

# Inicializa os valores iniciais da sequência de Fibonacci
fibonacci = [0, 1]

# Calcula a sequência de Fibonacci até encontrar um número maior ou igual ao número a ser verificado
while fibonacci[-1] < num:
    proximo_valor = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_valor)

# Verifica se o número pertence à sequência de Fibonacci
if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci")
