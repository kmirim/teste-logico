MAX_NOTA = 10.0

def media(num1, num2):
	return ((num1 + num2) / 2) 
def main():
	try:
		num1 = float(input("Informe a primeira nota: "))
		num2 = float(input("Informe a segunda nota: "))
		if num1 > MAX_NOTA or num2 > MAX_NOTA:
			print(f"As notas devem ser menores ou igual a 10.0")
			return
		result = media(num1, num2)
		if result >= 7:
			print(f"Média de {result}: APROVADO.")
		elif result < 7 or result >= 5:
			print(f"Média de {result}: PROVA FINAL.") 
		else:
			print(f"Média de {result}: REPROVADO.")
	except ValueError:
		print("Por favor, insira somente números!")
if __name__ == "__main__":
	main()
