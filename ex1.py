def factorial(num):
	if num < 0:
		return 0
	elif num == 0 or num == 1:
		return 1
	else:
		return num * factorial(num - 1)

def main ():
	try: 
		num = int (input("Informe um número para calcular o fatorial: "))
		result = factorial(num)
		print(f"O fatorial de {num} é {result}")
	except ValueError:
		print("Insira um numero inteiro")
if __name__ == "__main__":
	main()
