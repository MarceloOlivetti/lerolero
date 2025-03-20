import random 

parte1 = [
	"Frase A",
	"Frase B",
	"Frase 3"
	]
parte2 = [
	"Frase D",
	"Frase E",
	"Frase F"
 ]
parte3 = [
	"Frase H",
	"Frase I",
	"Frase J"

]

lingua = int(input("Escolha a língua: 1- português; 2- inglês\n "))

if lingua == 2:
	parte1 = []
	parte2 = []
	parte3 = []

print(random.choice(parte1),random.choice(parte2),random.choice(parte3))
