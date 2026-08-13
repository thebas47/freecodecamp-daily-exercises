def fibonacci_sequence(start_sequence, length):

    # Realizando um slice na lista "start sequence"
    # O slice é responsável por filtrar os casos de length 0 e 1
    fibonacci = start_sequence[:length]

    # Loop while responsável por manter a sequência na ordem delimitada pelo usuário
    while len(fibonacci) < length:
        # Fórmula Simples pra calculo de proximo numero da sequência de fibonacci
        next = fibonacci[-2] + fibonacci[-1]
        # Alimenta a lista
        fibonacci.append(next)
        
    return fibonacci

print(fibonacci_sequence([0, 1], 20))
print(fibonacci_sequence([21, 32], 1))
print(fibonacci_sequence([0, 1], 0))
print(fibonacci_sequence([10, 20], 2))
print(fibonacci_sequence([123456789, 987654321], 5))
