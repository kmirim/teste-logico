def fibonacci(i):
	if i < 0:
		return -1
	if i == 0:
        	return 0
	elif i == 1 or i == 2:
		return 1
	else:
		return fibonacci(i - 1) + fibonacci(i - 2)

def main():
	try:
		i = int(input("Informe um índice para calcular a sequência de Fibonacci: "))
		result = fibonacci(i)
		print(f"O valor da sequência de Fibonacci no índice {i} é {result}")
	except ValueError:
		print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
	main()
