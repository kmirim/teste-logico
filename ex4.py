def fibonacci(i):
    sequence = []
    a, b = 0, 1
    for _ in range(i):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    try:
        i = int(input("Informe um índice para calcular a sequência de Fibonacci: "))
        if i < 0:
            print("Por favor, insira um número inteiro não negativo.")
        else:
            result = fibonacci(i)
            print(" ".join(map(str, result)))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
