import math
import time

nummer = 1
tot = 37

#Normale Fibonacci functie
def fib(n):
	#Als het het 0de of 1ste element is,
	#gewoon 0 of 1 terug sturen
	if n <= 1:
		return n
	#Anders stuur de som van het vorige
	#en het element daar weer voor
	return fib(n-1)+fib(n-2)

#Wiskundige Fibonacci functie
def fib2(n):
	#Bereid wiskundige constanten voor
	phi = (1+math.sqrt(5))/2
	hoofdletterPhi = 1 - phi
	#(phi^n-Phi^n)/wortel5
	num = (math.pow(phi,n)-math.pow(hoofdletterPhi,n))/math.sqrt(5)
	return int(num)

#Een functie om de snelheid van een functie te testen
#Argumenten:
#func: de functie waarvan de snelheid getest moet worden
#x: Het argument voor die functie
#name: de naam voor de functie
def testtime(func,x,name = ""):
	#Mooi teskt en informatie weergeven
	print("\n\n=="+name+"==")
	print("running= \t"+str(func))
	print("with n = \t\033[91m"+str(x)+"\033[0m")
	#Pak de tijd voor de functie
	start = time.time()
	#Voer de functie met het argument uit
	res = func(x)
	#Pak de tijd na de functie
	end = time.time()
	#print het resultaat er tijd
	print("result = \t" + str(res))
	print("time   = \t" + '{:.20f}'.format(end-start))
	print("\n")
	#geef de tijd die de functie op nam terug
	return end-start

while nummer <= tot:
	testtime(fib,nummer,"FIB")
	testtime(fib2,nummer,"FAST")
	nummer = nummer +1
	raw_input()