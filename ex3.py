import math

def distance(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def main():
	try:
		x1 = float(input("Informe a coordenada x do primeiro ponto: "))
		y1 = float(input("Informe a coordenada y do primeiro ponto: "))
		x2 = float(input("Informe a coordenada x do segundo ponto: "))
		y2 = float(input("Informe a coordenada y do segundo ponto: "))

		p1 = (x1, y1)
		p2 = (x2, y2)
		ret = distance(p1, p2)
	
		print(f"A distância euclidiana entre {p1} e {p2} é {ret}")
	except ValueError:
		print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
	main() 
