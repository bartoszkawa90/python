
import random
import math


def Single(x,y):
	
	def F(x):
		return 1/(1+math.exp(-x))

	weights_1 = []
	for i in range(num_of_neu_1*num_of_inputs):
		weights_1.append(random.random())
	
	print(weights_1)
	print("Enter the input values")

	hiden_layer = [0]*num_of_neu_1
	inputs = []

	for i in range(num_of_inputs):
		inp = int(input(" Enter the ",i," input  "))
	        inputs.append(inp)

	sum = 0
	for i in range(num_of_neu_1):
	     	for j in range(num_of_neu_1):
         		sum += inputs[i] * weights_1[i+3*j] # wagi są mnożone w ten sposób że 11 21 31 idą do pierwszego splotu warstwy ukrytej
	     	hiden_layer[i] = F(sum)
 	print(hiden_layer)   # Prawidłowo wyznacza wartości warstwy ukrytej
